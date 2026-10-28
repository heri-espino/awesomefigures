# Branch consolidation — 2026-10-28

Repository: `heri-espino/awesomefigures` (personal fork).
The official organization repository is managed separately.

## Preserved on main

- Automatic manuscript publication feature: fork PR #1, squash-merged as
  `266492a770e0b5ee944d248fe0c861329c01d8c6`.
- The latest feature commit `7f7552d2df6fc6cf2904c5587e81cd4362caffc7`
  passed Python 3.10/3.12, strict Sphinx, and real LaTeX/PDF integration CI.
- Previous AwesomeFigures rename and Conda development changes had already
  been incorporated in upstream/fork main through earlier PR mergers.
- `feature/release-readiness-standards` was checked by Git tree ID:
  `4c79f7436e64800b5f5afb136a02acb355f727a6`, equal to this fork's
  newly merged main tree, hence no distinct file changes are discarded.

## Stale branch removal

A one-time guarded GitHub Actions cleanup checked each remote branch against
its audited commit SHA before deleting it. The cleanup **correctly refused**
to remove the concurrently updated release-readiness branch.

Verified removed:
- `feature/automatic-publication-workflow`
- `feature/conda-environment-awesomefigures-20261022`
- `refactor/awesomefigures-package`
- `refactor/rename-awesomefigures`

**Still active:** `feature/release-readiness-standards`. Its SHA changed
multiple times while cleanup was running and it contains unique release
documentation and standards work. It was deliberately preserved for a
separate review/merge and subsequent branch deletion. The fork may still have more than one branch while other contributors
are actively developing or reviewing new work. The temporary cleanup workflow was
removed after it successfully deleted the four stale branches.

Expected refs prior to cleanup:

- `feature/automatic-publication-workflow`: `7f7552d2df6fc6cf2904c5587e81cd4362caffc7`
- `feature/conda-environment-awesomefigures-20261022`: `8bd231fe4a6658626101be48ba4a581f658593a2`
- `feature/release-readiness-standards`: `a9760351c1f72ccf7a1a2ef2ff14136d6e280d88`
- `refactor/awesomefigures-package`: `baab2267c8134994b4dff4fb804ad3c9ed57f19e`
- `refactor/rename-awesomefigures`: `cc01f34d07e00e68e9e155186b0022008c272aaf`

Use feature branches for future PRs, then squash-merge and remove them.
Retain only `main` between tasks.

Do not force-push or rewrite `main`. Do not delete unmerged work whose
remote branch tip has changed since the audit.

## Concurrent work notice

After the verified cleanup, another branch `review/upstream-main-20261028`
was created, in addition to `feature/release-readiness-standards`.
Neither was deleted because they may be in use by another contributor.
Maintain `main` as the only **long-lived** branch; merge and remove these
temporary branches once their reviews and work are complete.
