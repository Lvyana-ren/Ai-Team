# Director Charter

The Director is the human user and the sole authority for:
- Product direction, goals, scope, priorities, and constraints.
- Approval of requirements and architecture.
- Approval to begin implementation.
- Acceptance of final work.
- Authorization to push, merge, release, deploy, flash, or perform destructive actions.

The four AI chats are advisory and execution roles, not independent authorities.

## Approval gates

A task must not advance past:
1. Discovery until the Director accepts the task brief.
2. Design until the Director approves the design/technical specification.
3. Implementation until the Director explicitly authorizes implementation.
4. Release until the Director explicitly accepts the final result and authorizes the release action.

## Manual handoff rule

The Director manually transfers the handoff document and referenced files to the next chat. The receiving chat must confirm the Task ID, version, sender, expected inputs, and next action before proceeding.

## Decisions

Record decisions in `director/decisions/<TASK-ID>-decisions.md`. Include date, decision, rationale, scope impact, and explicit approval status.
