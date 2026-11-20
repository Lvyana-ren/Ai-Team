# Third-Party Skill Sources

Selected upstream skill materials are vendored into `agents/<role>/skills/upstream/`. Most skills are curated Markdown snapshots; UI/UX Pro Max is vendored as a complete package including its search scripts, datasets, references, fixtures, and tests. Upstream content is preserved except for repository-specific script paths in its `SKILL.md`; provenance is recorded alongside the package.

- **mattpocock/skills** — https://github.com/mattpocock/skills — snapshot tree `5863806dd4e15c63174bee4e7515a4256792ecfa`
- **nextlevelbuilder/ui-ux-pro-max-skill** — https://github.com/nextlevelbuilder/ui-ux-pro-max-skill — complete UI/UX Pro Max package pinned to commit `2de1134dc4d1cfe112934611ae5803ae17a1bd7e` (80 upstream files plus repository-specific provenance/readme; script paths adapted for this repository)
- **emilkowalski/skills** — https://github.com/emilkowalski/skills — snapshot tree `64eb3deb9a5fbfa041faf783e0bc3fd635872e9c`
- **affaan-m/ECC** — https://github.com/affaan-m/ECC — snapshot tree `3f14a103a8694e51c1df9a806217a6d0b5f7a6f7`
- **chrisbanes/skills** — https://github.com/chrisbanes/skills — snapshot tree `2161b90dccbae48803a137291108cdc7e72bb4d3`

This repository is not a full clone of every upstream source repository. UI/UX Pro Max is the exception: its complete skill package is vendored so its local search workflow can run without fetching datasets at runtime. The exact upstream commit and local modifications are documented in `agents/designer/skills/upstream/ui-ux-pro-max/UPSTREAM.md`.


## Included license texts

The upstream license texts are preserved under `third-party-licenses/`:
- mattpocock/skills — MIT
- nextlevelbuilder/ui-ux-pro-max-skill — MIT
- emilkowalski/skills — MIT
- affaan-m/ECC — MIT
- chrisbanes/skills — Apache License 2.0

This repository contains selected upstream Markdown skills and a complete vendored UI/UX Pro Max package. External fonts, icon libraries, frameworks, and websites referenced by upstream catalog records retain their own licenses and terms; the vendored MIT license does not relicense those third-party assets.
