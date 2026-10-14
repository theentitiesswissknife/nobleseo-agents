"""Repository checks run by CI: manifests, versions, skills, license gate and a content scan.

Usage: python scripts/check_repo.py [ROOT]
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[1]

# The only accepted approval record: a CHANGELOG line in exactly this form.
APPROVAL = re.compile(r"^- License approved by the NobleSEO rights holder on \d{4}-\d{2}-\d{2}: [A-Za-z0-9.+-]+\.?$", re.M)
README_NOTICE = "No license has been granted yet. All rights are reserved by the NobleSEO rights holder"
LICENSE_NAMES = re.compile(r"^(?:LICEN[CS]E|COPYING|UNLICENSE)(?:[._-].*)?$", re.I)
SENSITIVE_NAMES = re.compile(r"^(?:\.env(?:\..*)?|.*\.(?:pem|key|p12|pfx)|id_(?:rsa|ed25519|ecdsa)(?:\.pub)?|\.npmrc|\.pypirc)$", re.I)

_OCTET = r"(?:25[0-5]|2[0-4]\d|1?\d?\d)"
# Content that must never be published (see docs/skill-publication-checklist.md).
FORBIDDEN = {
    "email address": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"),
    "absolute Windows path": re.compile(r"\b[A-Za-z]:[\\/](?:Users|Python|Windows|Program)", re.I),
    "home directory path": re.compile(r"/(?:home|Users)/[A-Za-z0-9._-]+/"),
    "private IP address": re.compile(
        rf"(?<![\d.])(?:10\.{_OCTET}|127\.{_OCTET}|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.{_OCTET}\.{_OCTET}(?![\d.])"
    ),
    "secret-like token": re.compile(
        r"(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}"
        r"|xox[abpr]-[A-Za-z0-9-]{10,}|AIza[0-9A-Za-z_-]{35}|-----BEGIN [A-Z ]*PRIVATE KEY-----)"
    ),
}
TEXT_SUFFIXES = {".md", ".py", ".json", ".csv", ".yml", ".yaml", ".txt", ".toml", ".cfg", ".ini", ""}


class Checker:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.plugin = root / "plugins" / "nobleseo"
        self.errors: list[str] = []

    def fail(self, message: str) -> None:
        self.errors.append(message)

    def files(self) -> list[Path]:
        """Every file that would be published: tracked plus untracked-but-not-ignored."""
        try:
            out = subprocess.run(
                ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
                cwd=self.root, capture_output=True, check=True,
            ).stdout.decode("utf-8")
            return sorted(self.root / name for name in out.split("\0") if name)
        except (OSError, subprocess.CalledProcessError):
            def skipped(part: str) -> bool:
                return part in {".git", "node_modules", "__pycache__", ".pytest_cache"} or part.startswith(".venv")

            return sorted(
                p for p in self.root.rglob("*")
                if p.is_file() and not any(skipped(part) for part in p.relative_to(self.root).parts)
            )

    def manifests(self) -> dict[str, dict]:
        paths = {
            "claude marketplace": self.root / ".claude-plugin" / "marketplace.json",
            "codex marketplace": self.root / ".agents" / "plugins" / "marketplace.json",
            "claude plugin": self.plugin / ".claude-plugin" / "plugin.json",
            "codex plugin": self.plugin / ".codex-plugin" / "plugin.json",
        }
        loaded = {}
        for label, path in paths.items():
            try:
                loaded[label] = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                self.fail(f"{label}: cannot read {path.relative_to(self.root)} ({exc})")
        return loaded

    def check_versions(self, manifests: dict[str, dict]) -> None:
        versions = {
            "claude plugin": manifests.get("claude plugin", {}).get("version"),
            "codex plugin": manifests.get("codex plugin", {}).get("version"),
            "claude marketplace": manifests.get("claude marketplace", {}).get("metadata", {}).get("version"),
        }
        released = re.findall(r"^## \[(\d+\.\d+\.\d+)\]", self.read("CHANGELOG.md"), re.M)
        versions["CHANGELOG latest"] = released[0] if released else None
        if len(set(versions.values())) != 1 or None in versions.values():
            self.fail(f"versions disagree: {versions}")

    def check_skills(self) -> None:
        skills = sorted((self.plugin / "skills").glob("*/SKILL.md"))
        if not skills:
            self.fail("no skills found")
        for skill in skills:
            rel = skill.relative_to(self.root)
            text = skill.read_text(encoding="utf-8")
            match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
            if not match:
                self.fail(f"{rel}: missing frontmatter")
                continue
            fields = dict(line.split(":", 1) for line in match.group(1).splitlines() if ":" in line)
            name = fields.get("name", "").strip()
            if name != skill.parent.name:
                self.fail(f"{rel}: name '{name}' must equal folder '{skill.parent.name}'")
            if len(fields.get("description", "").strip()) < 40:
                self.fail(f"{rel}: description missing or too short")
            if "## Requirements" not in text:
                self.fail(f"{rel}: missing '## Requirements' section")
            if not any((skill.parent / "evals").glob("*.md")):
                self.fail(f"{rel}: missing evals/*.md")

    def check_license_gate(self, manifests: dict[str, dict], files: list[Path]) -> None:
        approved = bool(APPROVAL.search(self.read("CHANGELOG.md")))
        found = [str(p.relative_to(self.root)) for p in files if LICENSE_NAMES.match(p.name)]
        found += [f"{label}: {path}" for label, data in manifests.items() for path in _license_keys(data)]
        if found and not approved:
            self.fail(f"license present without the recorded rights-holder approval line: {found}")
        if not approved and README_NOTICE not in self.read("README.md"):
            self.fail("README.md must keep the all-rights-reserved notice until a license is approved")

    def scan_content(self, files: list[Path]) -> None:
        for path in files:
            rel = path.relative_to(self.root)
            if SENSITIVE_NAMES.match(path.name):
                self.fail(f"{rel}: sensitive file must not be published")
                continue
            if path.suffix.lower() not in TEXT_SUFFIXES or not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for label, pattern in FORBIDDEN.items():
                for hit in pattern.finditer(text):
                    line = text.count("\n", 0, hit.start()) + 1
                    self.fail(f"{rel}:{line}: {label}")

    def read(self, name: str) -> str:
        try:
            return (self.root / name).read_text(encoding="utf-8")
        except OSError:
            self.fail(f"{name} is missing")
            return ""

    def run(self) -> list[str]:
        manifests = self.manifests()
        files = self.files()
        self.check_versions(manifests)
        self.check_skills()
        self.check_license_gate(manifests, files)
        self.scan_content(files)
        return self.errors


def _license_keys(value: object, path: str = "$") -> list[str]:
    """JSON paths of every key named like 'license' anywhere in a manifest."""
    hits: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            here = f"{path}.{key}"
            if re.fullmatch(r"licen[cs]es?", str(key), re.I):
                hits.append(here)
            hits += _license_keys(child, here)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            hits += _license_keys(child, f"{path}[{index}]")
    return hits


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_ROOT
    errors = Checker(root).run()
    for message in errors:
        print(f"FAIL {message}")
    print("ok" if not errors else f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
