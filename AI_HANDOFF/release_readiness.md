# Release-readiness foundation handoff

## Scope

This change does not publish to PyPI or alter existing MIT licensing.
It adds GitHub community, citation, security, provenance and packaging
safety files, plus source/sdist/wheel metadata validation.

## Important decisions

- Preserve `LICENSE` (MIT, copyright 2026 Heriberto Espino Montelongo).
- `CITATION.cff` identifies the original author, repository and source
  metadata version 0.1.0. No DOI or release date is invented.
- `ATTRIBUTION.md` documents the established named palettes and distinguishes
  their original sources from AwesomeFigures' own code license.
- `RELEASING.md` requires manual authorization for publishing or tagging.
- Source distributions include contributor/security/citation files through
  `MANIFEST.in`; wheels include the LICENSE through PEP 639 metadata.
- Source audit: `python tools/check_release.py`.
- Artifact audit after build:
  `python -m build && python tools/check_release.py --dist dist`.
- Canonical GitHub repository is `awesomefigures/awesomefigures`;
  the old `heri-espino/Colors` repository URL should no longer be
  advertised as current.
- GitHub Pages deployment may still use an older host until manually
  migrated. Avoid inventing an unverified URL.

## Next steps

1. Confirm PR CI: Python 3.10 and 3.12, source metadata audit,
   packaging integrity, Sphinx.
2. Review citation name details, policies and security contact options
   with the human maintainer.
3. If desired, configure private vulnerability reporting in organization
   settings; never publish sensitive security details.
4. Do not merge upstream without authorization; do not publish a package
   solely because its packaging checks pass.
