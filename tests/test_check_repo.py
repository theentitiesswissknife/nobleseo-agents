import importlib.util
import json
import shutil
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("check_repo", ROOT / "scripts" / "check_repo.py")
check_repo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_repo)

APPROVAL = "- License approved by the NobleSEO rights holder on 2027-01-31: Apache-2.0\n"


@pytest.fixture
def repo(tmp_path):
    # Copy only what would be published, so local environments never leak into the fixture.
    target = tmp_path / "repo"
    for source in check_repo.Checker(ROOT).files():
        destination = target / source.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    return target


def errors(root):
    return check_repo.Checker(root).run()


def add_changelog_line(root, line):
    path = root / "CHANGELOG.md"
    path.write_text(path.read_text(encoding="utf-8") + "\n### License\n" + line, encoding="utf-8")


def test_clean_repository_passes(repo):
    assert errors(repo) == []


@pytest.mark.parametrize("name", ["LICENSE", "plugins/nobleseo/LICENSE.md", "plugins/nobleseo/skills/gsc-visualization/COPYING"])
def test_license_file_anywhere_fails_without_approval(repo, name):
    (repo / name).write_text("text", encoding="utf-8")
    assert any("license present" in e for e in errors(repo))


def test_nested_license_field_fails(repo):
    path = repo / ".claude-plugin" / "marketplace.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["plugins"][0]["license"] = "Apache-2.0"
    path.write_text(json.dumps(data), encoding="utf-8")
    assert any("$.plugins[0].license" in e for e in errors(repo))


@pytest.mark.parametrize("line", [
    "- Not approved by the NobleSEO rights holder\n",
    "- License not approved by the NobleSEO rights holder on 2027-01-31: Apache-2.0\n",
    "- License approved by the NobleSEO rights holder\n",
])
def test_negated_or_vague_approval_does_not_count(repo, line):
    add_changelog_line(repo, line)
    (repo / "LICENSE").write_text("text", encoding="utf-8")
    assert any("license present" in e for e in errors(repo))


def test_exact_approval_line_allows_license(repo):
    add_changelog_line(repo, APPROVAL)
    (repo / "LICENSE").write_text("text", encoding="utf-8")
    assert not any("license" in e.lower() for e in errors(repo))


def test_readme_notice_is_required_until_approval(repo):
    readme = repo / "README.md"
    readme.write_text(readme.read_text(encoding="utf-8").replace(check_repo.README_NOTICE, "Licensed."), encoding="utf-8")
    assert any("all-rights-reserved notice" in e for e in errors(repo))


@pytest.mark.parametrize("name", [".env", "deploy.pem", "id_rsa"])
def test_sensitive_files_fail(repo, name):
    (repo / name).write_text("x", encoding="utf-8")
    assert any("sensitive file" in e for e in errors(repo))


@pytest.mark.parametrize("text,flagged", [
    ("server at " + ".".join(["10", "1", "2", "3"]), True),
    ("version 10.1.2", False),
    ("ratio 192.168", False),
    ("token ghp_" + "a" * 30, True),
    ("mail someone" + "@" + "example.org", True),
])
def test_content_scan(repo, text, flagged):
    (repo / "docs" / "note.md").write_text(text, encoding="utf-8")
    hit = any("note.md" in e for e in errors(repo))
    assert hit is flagged


@pytest.mark.parametrize("name", ["docs/snippet.js", "scripts/run.sh", "docs/page.html"])
def test_secrets_in_any_text_file_are_found(repo, name):
    (repo / name).write_text("const token = 'ghp_" + "b" * 30 + "'", encoding="utf-8")
    assert any(Path(name).name in e and "secret-like token" in e for e in errors(repo))


def test_utf16_text_is_still_scanned(repo):
    (repo / "docs" / "notes.txt").write_bytes(("token ghp_" + "c" * 30).encode("utf-16"))
    assert any("notes.txt" in e and "secret-like token" in e for e in errors(repo))


def test_nul_bytes_without_a_bom_are_rejected(repo):
    (repo / "docs" / "odd.md").write_bytes(b"a\x00b")
    assert any("odd.md" in e and "unsupported text encoding" in e for e in errors(repo))
