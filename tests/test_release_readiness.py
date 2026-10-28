"""Release metadata, legal files and citation are validated in CI."""
from pathlib import Path
import sys
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def test_release_readiness_source_metadata():
    result = subprocess.run(
        [sys.executable, "tools/check_release.py"],
        cwd=ROOT, check=False, capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stdout + "\n" + result.stderr


def test_release_policy_is_manual_and_license_is_preserved():
    release = (ROOT / "RELEASING.md").read_text(encoding="utf-8")
    assert "explicit" in release
    assert "TestPyPI" in release
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert "MIT License" in license_text
    assert "Heriberto Espino Montelongo" in license_text
