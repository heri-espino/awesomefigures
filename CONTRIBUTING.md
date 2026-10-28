# Contributing to AwesomeFigures

Thank you for improving AwesomeFigures. Please use the canonical
[organization repository](https://github.com/awesomefigures/awesomefigures).
The project is MIT-licensed; submissions must be code, documentation, tests,
or figures that you are entitled to contribute under that license.

## Before starting

Read the [README](README.md), [feature inventory](FEATURES.md),
[agent instructions](AGENTS.md), and relevant documentation or tests.
Search existing issues and pull requests before opening duplicates.
For larger API or architectural changes, describe the problem in an issue
before implementing a new framework.

## Development setup

Use Python 3.10 or newer. Choose either Conda or a virtual environment.
From the repository root:

```bash
conda env create -f environment.yml
conda activate awesomefigures
python -m pip install -e ".[dev,docs,publication]"
```

Or with a pre-existing Python environment:

```bash
python -m pip install -e ".[dev,docs,publication]"
```

On a Unix shell or PowerShell, run:

```bash
python -m pytest
python -m sphinx -W -b html docs/source docs/_build/html
node tools/test_studio_smoke.js
```

TeX integration needs a separate local TeX distribution (MiKTeX on
Windows or TeX Live on Linux/macOS), with PGF and preview packages.
Use the dedicated GitHub Actions integration test for real PDF font
embedding and physical dimensions. Ordinary styling contributors
do not need TeX for every development edit.

## Pull-request workflow

1. Fork the organization repository or create a feature branch; do not
   commit directly to `main`.
2. Keep changes focused and follow existing style/public-API conventions.
3. Add tests for bug fixes and document new exported APIs in Sphinx and
   the feature inventory. Existing import paths should remain compatible
   unless an explicitly documented breaking change is approved.
4. For publication changes, keep plot regeneration separate from statistical
   computation. Use deterministic, already-computed input arrays.
5. Do not commit passwords, tokens, private TeX manuscripts, virtual
   environments, caches, or unnecessary generated binaries. Preserve useful
   scripts, configurations, verification reports, and handoff notes.
6. Include a concise before/after example, tested Python versions,
   CI links, any optional dependencies, limitations, and screenshots or
   technical PDFs when they materially clarify a visual change.
7. Submit a PR to the organization's `main`. Maintain the branch while
   reviews and CI are ongoing. Do not merge without approval.

Experiments, if needed, should be sequentially named `experiment001`,
`experiment002`, etc. Each must document motivation, reproduction
steps, results, failures, and next steps.

## Code, fonts, and third-party content

Use explicit, meaningful names and preserve provenance. The established
named palettes have original source attribution in
[ATTRIBUTION.md](ATTRIBUTION.md) and in their API metadata.
Do not assume an accessible palette is universally accessible.
Do not add third-party fonts or images unless redistribution is permitted
and the relevant license/credit is recorded.

## Conduct and support

Please follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). For ordinary questions,
see [SUPPORT.md](SUPPORT.md); for suspected vulnerabilities, follow
[SECURITY.md](SECURITY.md) rather than posting details in public issues.

All contributions are reviewed; acceptance is not guaranteed.
