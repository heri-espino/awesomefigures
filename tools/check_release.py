"""Check source-tree metadata and, optionally, actual sdist/wheel contents.

Use before any release; this is validation, not publication.
    python tools/check_release.py
    python -m build
    python tools/check_release.py --dist dist
"""
from __future__ import annotations

import argparse
import re
import tarfile
import zipfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "LICENSE",
    "README.md",
    "CITATION.cff",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "RELEASING.md",
    "ATTRIBUTION.md",
)
UPSTREAM = "https://github.com/awesomefigures/awesomefigures"


def validate_repository() -> None:
    missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
    if missing:
        raise AssertionError(f"Required release files missing: {missing}")
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert license_text.startswith("MIT License\n")
    assert "Copyright (c) 2026 Heriberto Espino Montelongo" in license_text
    citation = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
    assert citation["cff-version"] == "1.2.0"
    assert citation["type"] == "software"
    assert citation["title"] == "AwesomeFigures"
    assert citation["license"] == "MIT"
    assert citation["repository-code"] == UPSTREAM
    assert citation["authors"]
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert 'name = "awesomefigures"' in pyproject
    assert 'license = "MIT"' in pyproject
    assert 'license-files = ["LICENSE"]' in pyproject
    assert 'Homepage = "' + UPSTREAM + '"' in pyproject
    assert 'Source = "' + UPSTREAM + '"' in pyproject
    match = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, re.MULTILINE)
    assert match, "No project version in pyproject.toml"
    assert match.group(1) == citation["version"], "Citation and package versions differ"
    manifest = (ROOT / "MANIFEST.in").read_text(encoding="utf-8")
    for name in REQUIRED_FILES:
        assert f"include {name}" in manifest, f"MANIFEST.in omits {name}"
    print("Repository release metadata: PASS")


def validate_distributions(directory: Path) -> None:
    sdists = sorted(directory.glob("awesomefigures-*.tar.gz"))
    wheels = sorted(directory.glob("awesomefigures-*.whl"))
    if not sdists or not wheels:
        raise AssertionError("Build both a source distribution and a wheel first.")
    for sdist in sdists:
        with tarfile.open(sdist, "r:gz") as archive:
            members = set(archive.getnames())
            for file in REQUIRED_FILES:
                assert any(path.endswith("/" + file) for path in members), (
                    f"{sdist.name} missing {file}"
                )
            assert any(path.endswith("/src/awesomefigures/__init__.py") for path in members)
        print(f"sdist {sdist.name}: PASS")
    for wheel in wheels:
        with zipfile.ZipFile(wheel) as archive:
            names = archive.namelist()
            assert any(x.startswith("awesomefigures/") for x in names)
            assert any(x.endswith("/LICENSE") and ".dist-info/" in x for x in names), (
                f"{wheel.name} missing LICENSE in wheel metadata"
            )
            assert any(x.endswith(".dist-info/METADATA") for x in names)
            data = next(archive.read(x).decode("utf-8") for x in names
                        if x.endswith(".dist-info/METADATA"))
            assert "Name: awesomefigures" in data
            assert "License-Expression: MIT" in data or "License: MIT" in data
            assert UPSTREAM in data
        print(f"wheel {wheel.name}: PASS")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, help="Folder containing built distributions")
    args = parser.parse_args()
    validate_repository()
    if args.dist is not None:
        validate_distributions(args.dist)
    print("Release checks passed; this command does not upload packages.")


if __name__ == "__main__":
    main()
