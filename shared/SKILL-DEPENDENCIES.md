# Skill and Environment Prerequisites

This is an inventory template and reporting policy, not a claim that every tool is installed or required for every task. Requirements are task- and skill-specific. The selected skill's own instructions take precedence.

## Status values
- available: checked and usable in the current execution environment.
- unavailable: checked and missing, inaccessible, or unusable.
- not_applicable: not required by the selected task procedure.
- not_checked: not verified; do not assume availability.

## Common prerequisite categories
| Prerequisite | Typical use | How to report |
|---|---|---|
| GitHub repository access | Inspect source, branches, commits, PRs, or update files | State repository/ref and actual permission/tool result |
| Python 3 | Skills or scripts that explicitly require Python | Record version and exact script/command executed |
| Gradle + JDK | Android/JVM Gradle builds and tests | Record Gradle/JDK versions and exact task/command |
| Kotlin compiler + JVM | Standalone Kotlin/JVM compilation or tests | Record compiler/JVM versions and exact commands |
| Android SDK / build tools | Android app builds, lint, packaging, device tooling | Record installed components and versions |
| Android device / emulator | Runtime, UI, performance, compatibility validation | Record device/API/build and exact test performed |
| Kernel toolchain | Kernel compilation and image packaging | Record compiler, linker, build config, target architecture |
| Flash/recovery access | Device flashing and boot validation | Requires explicit Director authorization; never infer permission |

## Required per-task prerequisite record
| Prerequisite | Required by skill/work item | Status | Evidence / version | Impact if unavailable |
|---|---|---|---|---|
| | | not_checked | | |

## Rules
1. Do not list a prerequisite as available without checking it in the current environment.
2. Do not treat an installed skill as proof that its external tools or runtime prerequisites exist.
3. If a prerequisite is missing, block only the procedure/check that depends on it unless the task has a true dependency that prevents all further work.
4. Continue independent, authorized checks where possible, following shared/SKILL-ENFORCEMENT.md.
5. Never use an alternative tool or command when the selected skill explicitly prohibits that fallback.
6. Clearly separate source inspection, static analysis, compilation, test execution, device validation, and release validation.
7. Flashing, destructive operations, publishing, deployment, and release require explicit Director authorization regardless of tool availability.