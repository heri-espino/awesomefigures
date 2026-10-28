# Release checklist

This is an **operator's checklist**, not an automated publication workflow.
Publishing to PyPI or creating a GitHub Release always requires a maintainer's
explicit decision. Never store PyPI tokens or signing keys in Git.

## 1. Prepare a reviewed release

- Confirm the licensing and provenance of code, fonts, screenshots, and
  included data. `LICENSE` is MIT; see `ATTRIBUTION.md` for palette sources.
- Review open issues, compatibility, deprecations, security concerns,
  contributors, and Sphinx documentation.
- Update the version consistently in `pyproject.toml`,
  `src/awesomefigures/__init__.py`, `docs/source/conf.py`, and
  `CITATION.cff`. Avoid inventing release dates or DOIs.
- Move appropriate `[Unreleased]` items to a dated release heading in
  `CHANGELOG.md`.
- Ensure the canonical GitHub organization links and current public
  documentation link are correct before tagging.
- Obtain PR review and merge approval for the release commit.

## 2. Validate before tagging

From a clean checkout:

```bash
python -m pip install -e ".[dev,docs,publication,release]"
python -m pytest
node tools/test_studio_smoke.js
python -m sphinx -W -b html docs/source docs/_build/html
python tools/check_release.py
python -m build
python -m twine check dist/*
python tools/check_release.py --dist dist
```

The dedicated TeX Live/MiKTeX integration workflow must pass before making
claims about exact publication PDF fonts/dimensions. Visually inspect a
representative final PDF, including a two-column and a multi-panel figure.
`python tools/check_release.py --dist dist` verifies that built wheel and
sdist contain the relevant license and metadata files.

## 3. Test the built artifact

Create a disposable virtual environment and install the wheel, not the
editable source tree. Confirm `import awesomefigures as af` and smoke-test
a figure. Verify supported Python versions (3.10 and 3.12 in current CI)
and optional `publication` dependencies. The wheel build is platform-neutral
Python; native TeX remains an external optional prerequisite.

## 4. Publish intentionally

Only after approval, create a version tag from the reviewed `main` commit
and publish a GitHub Release with changelog notes. Use an explicitly
configured PyPI/TestPyPI trusted-publishing workflow or an authorized
maintainer session. Do not add hard-coded credentials.

A TestPyPI dry run is optional but recommended. Confirm the target project
name and publisher authorization before any upload. If publishing through
`twine`, use the explicit target and review package contents first;
`twine upload dist/*` is a **manual release action**, not a CI test.

Verify the published archive, install it in a clean environment, update
documentation, and record the tagged commit/CI evidence in the release notes.

## 5. Preserve provenance

Commit source, tests, packaging configuration, handoff documentation, release
notes and reproducible figure-verification artifacts. Never rerun unrelated
statistical experiments as part of a package release.
