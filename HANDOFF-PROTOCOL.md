# Xen AI Multi-Chat Handoff Protocol

## Manual transfer model

No chat is assumed to have access to another chat's history. The Director is the human relay:
1. Chat A creates a handoff document.
2. Director saves it in the GitHub task folder, including the Skill Usage Record.
3. Director opens Chat B and supplies the handoff plus referenced files (upload/paste, or authorized GitHub connection).
4. Chat B verifies Task ID, version, sender, approval status, and required inputs.
5. Chat B performs only its role and returns its deliverables and next handoff.
6. Director saves the outputs and manually passes them to the next chat.

## Required versioning

Use `<TASK-ID>-<ROLE>-v<MAJOR.MINOR>`, e.g. `XENOS-001-DESIGNER-v1.0`.

If an upstream document changes, downstream work based on the old version is stale. Mark it `SUPERSEDED` and request a new handoff.

## Handoff acceptance checklist

Receiving chat must confirm:
- Task ID matches.
- Handoff version is latest.
- Sender and recipient are correct.
- Required documents are present and readable.
- Director approval exists for the next stage.
- Scope and acceptance criteria are unambiguous.

If any check fails, do not proceed. Return `BLOCKED` with the missing item.

## Revision loop

Reviewer `NEEDS_CHANGES` -> Director reviews findings -> Director authorizes revision -> Programmer revises -> Reviewer rechecks.

Reviewer does not directly send unapproved scope changes to Programmer. Director decides whether findings are in scope.

After three unsuccessful review cycles, stop and ask Director for a recovery decision.

## GitHub commit convention

- `docs(XENOS-001): add approved task brief`
- `design(XENOS-001): add launcher specifications`
- `feat(XENOS-001): implement launcher shell`
- `review(XENOS-001): add independent review report`

Do not commit generated secrets, raw private logs, API keys, or unrelated files.

## Director's manual relay prompt

Use this when passing work to a department:

"Continue Task <TASK-ID> as <ROLE>. Treat the attached handoff and referenced repository files as the source of truth. First verify Task ID, version, approvals, required inputs, and scope. If anything is missing or inconsistent, stop and report BLOCKED. Perform only your assigned role. Return deliverables and a completed next-agent handoff using the standard template. Do not claim GitHub was updated unless you actually had authorized repository access and completed the change."
