# Mandatory Skill Enforcement Policy

## Before work
- No agent starts task execution before reading its SKILL-INDEX.md and completing the mandatory preflight gate in its identity.
- Read each selected skill's full SKILL.md and local references/examples required by the procedure. A directory listing or skill title is not enough.
- Use supporting scripts/data when the skill explicitly requires them and those assets are available.
- Record exact skill paths, applicability, and concrete steps applied in the task handoff/report.

## Missing skill
Stop the affected task procedure with BLOCKED_SKILL_UNAVAILABLE; identify the missing path and request Director guidance. Do not invent the skill's contents or silently replace it with general knowledge.

## Missing environment prerequisite
A skill being present does not mean its runtime prerequisites are available. Record each prerequisite as available, unavailable, not_applicable, or not_checked.
If a required prerequisite is unavailable, mark the affected validation/procedure as blocked and explain the impact. Do not claim that it ran. Do not silently substitute another tool when the skill explicitly prohibits fallback.

## Partial execution rule
A blocker applies only to work that depends on it. Continue other independent, authorized checks that do not depend on the missing skill, tool, access, or environment. Examples:
- Gradle unavailable: source, test assertions, archive structure, and supplied logs may still be inspected independently.
- GitHub access unavailable: supplied archives and source snapshots may still be inspected.
- Test runtime unavailable: static test/source inspection may continue, but tests must be reported as not executed.
- Device unavailable: source/build checks may continue, but device compatibility or runtime behavior must not be claimed.

Do not bypass a skill's explicit prohibition. Partial execution does not authorize a prohibited fallback or unsafe action.

## During and after work
Follow the selected skill's procedure. Include a Skill Usage Record with path, reason, applied step, and resulting artifact/evidence. Reviewer verifies the record against supplied artifacts.

Report each validation item separately as passed, failed, blocked, not_run, or not_applicable. A task may be partially completed while one or more checks are blocked. The overall workflow status and any review verdict must state that limitation clearly.

## Enforcement limitation
This is an auditable procedural gate. Markdown alone cannot technically prevent a chat model from ignoring it. A future agent runtime can strengthen it with pre-task hooks that validate file reads before allowing work.