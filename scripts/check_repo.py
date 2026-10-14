"""Repository checks run by CI: manifests, versions, skills, license gate and a basic content scan."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "nobleseo"
MANIFESTS = {
    "claude marketplace": ROOT / ".claude-plugin" / "marketplace.json",
    "codex marketplace": ROOT / ".agents" / "plugins" / "marketplace.json",
    "claude plugin": PLUGIN / ".claude-plugin" / "plugin.json",
    "codex plugin": PLUGIN / ".codex-plugin" / "plugin.json",
}
# Content that must never be published (see docs/skill-publication-checklist.md).
FORBIDDEN = {
    "email address": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "absolute Windows path": re.compile(r"\b[A-Za-z]:[\\/](?:Users|Python|Windows|Program)", re.I),
    "home directory path": re.compile(r"/(?:home|Users)/[A-Za-z0-9._-]+/"),
    "private IP address": re.compile(r"\b(?:10|127|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}(?:\.\d{1,3})?\b"),
    "secret-like token": re.compile(r"\b(?:sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[bp]-[A-Za-z0-9-]{10,})"),
}
SCANNED_SUFFIXES = {".md", ".py", ".json", ".csv", ".yml", ".yaml", ".txt"}
SKIP_SCAN = {ROOT / "scripts" / "check_repo.py"}

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def load_manifests() -> dict[str, dict]:
    loaded = {}
    for label, path in MANIFESTS.items():
        try:
            loaded[label] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"{label}: cannot read {path.relative_to(ROOT)} ({exc})")
    return loaded


def check_versions(manifests: dict[str, dict]) -> None:
    versions = {
        "claude plugin": manifests.get("claude plugin", {}).get("version"),
        "codex plugin": manifests.get("codex plugin", {}).get("version"),
        "claude marketplace": manifests.get("claude marketplace", {}).get("metadata", {}).get("version"),
    }
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    released = re.findall(r"^## \[(\d+\.\d+\.\d+)\]", changelog, re.M)
    versions["CHANGELOG latest"] = released[0] if released else None
    if len(set(versions.values())) != 1 or None in versions.values():
        fail(f"versions disagree: {versions}")


def check_skills() -> None:
    skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    if not skills:
        fail("no skills found")
    for skill in skills:
        text = skill.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not match:
            fail(f"{skill.relative_to(ROOT)}: missing frontmatter")
            continue
        fields = dict(line.split(":", 1) for line in match.group(1).splitlines() if ":" in line)
        name = fields.get("name", "").strip()
        if name != skill.parent.name:
            fail(f"{skill.relative_to(ROOT)}: name '{name}' must equal folder '{skill.parent.name}'")
        if len(fields.get("description", "").strip()) < 40:
            fail(f"{skill.relative_to(ROOT)}: description missing or too short")
        if "## Requirements" not in text:
            fail(f"{skill.relative_to(ROOT)}: missing '## Requirements' section")
        if not any((skill.parent / "evals").glob("*.md")):
            fail(f"{skill.relative_to(ROOT)}: missing evals/*.md")


def check_license_gate(manifests: dict[str, dict]) -> None:
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    approved = re.search(r"^### License\n(?:- .*\n)*- .*approved by the NobleSEO rights holder", changelog, re.M | re.I)
    licensed = [p.name for p in ROOT.iterdir() if p.name.upper().startswith(("LICENSE", "LICENCE", "COPYING"))]
    licensed += [label for label, data in manifests.items() if "license" in data]
    if licensed and not approved:
        fail(f"license present without recorded rights-holder approval: {licensed}")


def scan_content() -> None:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SCANNED_SUFFIXES or path in SKIP_SCAN:
            continue
        if any(part in {".git", ".venv", "node_modules", "charts"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in FORBIDDEN.items():
            for hit in pattern.finditer(text):
                line = text.count("\n", 0, hit.start()) + 1
                fail(f"{path.relative_to(ROOT)}:{line}: {label}")


def main() -> int:
    manifests = load_manifests()
    check_versions(manifests)
    check_skills()
    check_license_gate(manifests)
    scan_content()
    for message in errors:
        print(f"FAIL {message}")
    print("ok" if not errors else f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
