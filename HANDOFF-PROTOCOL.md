# AI Team Multi-Chat Handoff Protocol

## Manual transfer model
No chat is assumed to have access to another chat's history. The Director is the human relay:
1. Chat A creates a handoff document and updates the task artifact manifest.
2. Director saves the handoff and artifacts in the GitHub task folder.
3. Director opens Chat B and supplies the handoff plus referenced files (upload/paste, or authorized GitHub connection).
4. Chat B verifies Task ID, version, sender, recipient, approval status, required inputs, and artifact integrity where hashes are supplied.
5. Chat B performs only its role and returns its deliverables and next handoff.
6. Director saves the outputs and manually passes them to the next chat.

A file path or filename alone does not prove that an artifact was transferred or inspected. The receiving agent must state which artifacts it could actually access.

## Workflow status versus review verdict
Workflow status describes progress:
- draft: being prepared; not ready for downstream execution.
- ready: required inputs and approvals for the next stage are present.
- in_progress: authorized work is underway.
- blocked: the next required action cannot proceed.
- needs_changes: a required correction is outstanding.
- completed: assigned work is complete; this does not imply Director acceptance or release approval.
- superseded: replaced by a newer task/handoff version.

Review verdict is used only when an independent review was performed:
- pass: reviewed against scope and acceptance criteria; no blocking findings.
- pass_with_observations: pass with documented non-blocking observations.
- conditional_pass: acceptance depends on explicitly stated conditions.
- reject: material findings prevent acceptance.
- insufficient_evidence: review attempted but evidence is inadequate.
- not_reviewed: no independent review was performed.

Do not use a review verdict as a workflow status. A Programmer may report workflow completed; only the Reviewer supplies a review verdict, and only the Director accepts the final result.

## Required versioning
Use TASK-ID-ROLE-vMAJOR.MINOR, e.g. AITEAM-001-DESIGNER-v1.0.
If an upstream document changes, downstream work based on the old version is stale. Mark it superseded and request a new handoff.

## Dependency-aware orchestration
For multi-agent or multi-stage tasks, the Orchestrator must provide:
1. Work breakdown with unique work-item IDs.
2. Agent assignment matrix (role, deliverable, authority boundary).
3. Dependency graph/order, including safe parallel work and blocking dependencies.
4. Acceptance criteria for each work item.
5. Risk and environment-prerequisite register.
6. Manual handoff sequence and Director approval gates.

Do not claim that an agent was delegated work merely because its name appears in a plan. Handoffs are manual; produce a ready-to-send package for the Director.

## Handoff acceptance checklist
Receiving chat must confirm:
- Task ID matches.
- Handoff version is latest.
- Sender and recipient are correct.
- Required documents are present and readable.
- Artifact references resolve and hashes match when supplied.
- Director approval exists for the next stage.
- Scope and acceptance criteria are unambiguous.

If any check fails, do not proceed with the affected work. Return blocked and identify the missing or inconsistent item. Independent authorized checks may continue under shared/SKILL-ENFORCEMENT.md.

## Revision loop
Reviewer needs_changes finding -> Director reviews findings -> Director authorizes revision -> Programmer revises -> Reviewer rechecks.
Reviewer does not directly send unapproved scope changes to Programmer. Director decides whether findings are in scope.
After three unsuccessful review cycles, stop and ask Director for a recovery decision.

## GitHub commit convention
- docs(AITEAM-001): add approved task brief
- design(AITEAM-001): add launcher specifications
- feat(AITEAM-001): implement launcher shell
- review(AITEAM-001): add independent review report

Do not commit generated secrets, raw private logs, API keys, or unrelated files.

## Director's manual relay prompt
"Continue Task <TASK-ID> as <ROLE>. Treat the attached handoff and referenced repository files as the source of truth. First verify Task ID, version, approvals, required inputs, artifact access/integrity, and scope. If anything is missing or inconsistent, stop the affected work and report BLOCKED; continue only independent authorized checks. Perform only your assigned role. Return deliverables and a completed next-agent handoff using the standard template. Do not claim GitHub was updated unless you actually had authorized repository access and completed the change."