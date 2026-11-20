# Xen AI Multi-Chat Team

**Mode:** Manual handoff · Four departments · GitHub as shared memory/source of truth.

This package defines four separate ChatGPT conversations:
1. XEN-ORCHESTRATOR
2. XEN-DESIGNER
3. XEN-PROGRAMMER
4. XEN-REVIEWER

The user is the Director and final decision-maker.

## Important operating model
Separate ChatGPT conversations do not automatically communicate, inspect each other's chat history, or run in the background. The GitHub repository is the shared record. The Director manually copies the relevant handoff instruction/document from one chat into the next chat.

A chat can only inspect GitHub content if an appropriate GitHub connection/tool is available and authorized. Otherwise, the Director uploads or pastes the needed files. Never claim a repository was read or modified unless that actually happened.

## Repository layout
This repository is the central team repository. Each agent has a curated upstream skill library under agents/<role>/skills/upstream/.

~~~text
Xen-AI-Team/
├── README.md
├── director/
├── agents/
│   ├── orchestrator/
│   ├── designer/
│   ├── programmer/
│   └── reviewer/
├── tasks/
├── shared/
│   ├── schemas/
│   └── templates/
└── archive/
~~~

## Setup
1. Create a private or public GitHub repository named Xen-AI-Team. Prefer private if task documents may contain proprietary source details.
2. Create four separate ChatGPT conversations.
3. In each conversation, provide the corresponding role IDENTITY.md, skills/SKILL-INDEX.md, and relevant full skill files. Use authorized GitHub access or attach/paste the files.
4. Every agent must pass the mandatory skill preflight gate in shared/SKILL-ENFORCEMENT.md before work.
5. Keep each conversation dedicated to its role.
6. For each task, create a unique Task ID and task folder.
7. Pass handoffs manually using shared/templates/handoff.md and include the Skill Usage Record.
8. For tasks that produce or transfer files, maintain an artifact-manifest.json using shared/schemas/artifact-manifest.schema.json.

## First message for each chat
After providing its identity, skill index, and relevant full skill files, send:

> You are now operating as the Xen AI Team role defined in the provided identity and skills. Treat those documents as your operating contract. Confirm your role, authority limits, required inputs, output files, and handoff format. Do not begin a task until I provide a Task ID and task brief.

## Four chat identities
- Orchestrator: receives Director's request, clarifies requirements, creates task brief and dependency-aware delegation package. Does not approve its own plan.
- Designer: produces implementation-ready UI/UX and motion specifications. Does not implement app code.
- Programmer: implements only approved scope. Does not self-review or approve release.
- Reviewer: independently inspects supplied diff/files and evidence. Read-only; does not fix code.

## Workflow states and review verdicts
Workflow status and review outcome are separate fields. Workflow status describes progress (draft, ready, in_progress, blocked, needs_changes, completed, superseded). Review verdict is used only after an actual independent review (pass, pass_with_observations, conditional_pass, reject, insufficient_evidence, not_reviewed). See HANDOFF-PROTOCOL.md.

## Source of truth
Priority order:
1. Explicit latest Director decision for the Task ID.
2. Approved task brief and approved design/technical specification.
3. Latest versioned handoff document.
4. Repository source and test evidence.
5. Chat conversation context.

If documents conflict, stop and ask Director. Do not silently reconcile.

## Security
- Do not commit API keys, passwords, private keys, signing keys, tokens, or personal data.
- Redact secrets from logs and screenshots.
- Do not run destructive commands or flash devices based on a chat instruction alone.
- Do not push, merge, publish, deploy, or release without explicit Director approval.
- Reviewer receives the smallest useful diff and evidence; do not expose unrelated secrets.

## Skill library and operational policy
- Role-specific catalogs: agents/<role>/skills/SKILL-INDEX.md
- Mandatory preflight, partial execution, and usage reporting: shared/SKILL-ENFORCEMENT.md
- Environment prerequisite inventory: shared/SKILL-DEPENDENCIES.md
- Handoff protocol: HANDOFF-PROTOCOL.md
- Artifact provenance schema: shared/schemas/artifact-manifest.schema.json
- Handoff schema/template: shared/schemas/handoff.schema.json, shared/templates/handoff.md
- Upstream provenance: THIRD-PARTY-SKILLS.md