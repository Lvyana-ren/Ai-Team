# UI/UX Pro Max — Upstream Provenance

- **Upstream:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- **Upstream source directory:** `.claude/skills/ui-ux-pro-max/`
- **Pinned commit:** `2de1134dc4d1cfe112934611ae5803ae17a1bd7e`
- **Vendored on:** 2026-11-19
- **Upstream license:** MIT — Copyright (c) 2024 Next Level Builder
- **Upstream files:** 80 (SKILL.md, references, Python scripts, script tests/fixtures, CSV/JSON catalogs including stack data)

## Local layout

This package is stored under `agents/designer/skills/upstream/ui-ux-pro-max/`. The upstream `SKILL.md` has one repository-specific adaptation: commands now reference `$XEN_AI_TEAM_ROOT/agents/designer/skills/upstream/ui-ux-pro-max/scripts/search.py` rather than the upstream Claude plugin root. The search engine and data files remain unmodified from the pinned upstream snapshot.

Before running a command, set the root variable from a local checkout:

```bash
export XEN_AI_TEAM_ROOT="$(git rev-parse --show-toplevel)"
python "$XEN_AI_TEAM_ROOT/agents/designer/skills/upstream/ui-ux-pro-max/scripts/search.py" "dark dashboard" --domain style
```

The scripts use Python 3 standard-library modules; no runtime package installation or network access is required for catalog search. Run from a local checkout with Python 3 available. If the current agent environment cannot execute repository scripts, it may still use the vendored Markdown references, but it must not claim that a catalog query was run.

## Integrity and licensing

The vendored data, scripts, and references are copied from the pinned upstream commit. The upstream MIT license is included as `LICENSE.txt`. Keep this notice and the copyright/license text with redistributed copies. Catalog entries may refer to external fonts, icons, frameworks, or services; those referenced assets remain subject to their own terms.

## Update procedure

1. Select and record a specific upstream commit.
2. Compare the complete `.claude/skills/ui-ux-pro-max/` file tree against this directory.
3. Sync all files, preserving the upstream directory structure and license.
4. Reapply only the documented repository-path adaptation in `SKILL.md`.
5. Run search smoke tests and the upstream test suite where the environment permits.
6. Update this file and `THIRD-PARTY-SKILLS.md` with the new pinned commit.
