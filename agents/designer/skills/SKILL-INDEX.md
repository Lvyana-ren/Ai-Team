# Designer Skill Index

Read each selected skill's complete `SKILL.md` and relevant local references/examples before producing a design deliverable.

| Skill | Trigger / capability | Path |
|---|---|---|
| ui-ux-pro-max | UI/UX, visual direction, design systems, accessibility | `upstream/ui-ux-pro-max/` |
| animate | Create motion/transition behavior | `upstream/emil/animate/` |
| review-animations | Critique existing motion | `upstream/emil/review-animations/` |
| find-animation-opportunities | Audit screens for useful motion | `upstream/emil/find-animation-opportunities/` |
| animation-performance | Motion/rendering performance | `upstream/emil/animation-performance/` |
| gestures | Gesture interaction design | `upstream/emil/gestures/` |
| mobile-native | Native mobile interaction conventions | `upstream/emil/mobile-native/` |
| compose-animations | Compose motion API choices; Compose only | `upstream/chris-banes/compose-animations/` |
| compose-component-design | Compose API/slot design; Compose only | `upstream/chris-banes/compose-component-design/` |

**Required every UI task:** `ui-ux-pro-max`. Add motion/Compose skills only when relevant. Do not apply Compose guidance to Views/Launcher3 or another UI toolkit.

**Vendored package:** the complete upstream UI/UX Pro Max package is included: `SKILL.md`, `references/`, `scripts/` (including tests and fixtures), and `data/` (including stack-specific CSVs). The snapshot is pinned and documented in `upstream/ui-ux-pro-max/UPSTREAM.md`. Before using the CLI, set `XEN_AI_TEAM_ROOT` to the local Xen-AI-Team repository root (for example, `export XEN_AI_TEAM_ROOT="$(git rev-parse --show-toplevel)"`) and ensure Python 3 is available. Run the search script using the full repository-relative path shown in `SKILL.md`. If Python execution is unavailable in the current chat/runtime, report that limitation; do not claim a CLI search was executed.
