# Mandatory Skill Enforcement Policy

## Before work
- No agent starts task execution before reading its `SKILL-INDEX.md` and completing the mandatory preflight gate in its identity.
- Read each selected skill's full `SKILL.md` and local references/examples required by the procedure. A directory listing or skill title is not enough.
- Use supporting scripts/data when the skill explicitly requires them and those assets are available.
- Record exact skill paths, applicability, and concrete steps applied in the task handoff/report.

## Missing skill
Stop with `BLOCKED_SKILL_UNAVAILABLE`; identify the missing path and request Director guidance. Do not invent the skill's contents or silently replace it with general knowledge.

## During and after work
Follow the selected skill's procedure. Include a Skill Usage Record with path, reason, applied step, and resulting artifact/evidence. Reviewer verifies the record against the supplied artifacts.

## Enforcement limitation
This is an auditable procedural gate. Markdown alone cannot technically prevent a chat model from ignoring it. A future agent runtime can strengthen it with pre-task hooks that validate file reads before allowing work.
