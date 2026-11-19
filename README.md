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

Copy the `github-template/` contents into a central repository, e.g. `Xen-AI-Team`.

```text
Xen-AI-Team/
├── README.md
├── director/
│   ├── director-charter.md
│   └── decisions/
├── agents/
│   ├── orchestrator/
│   │   ├── IDENTITY.md
│   │   └── skills/
│   ├── designer/
│   │   ├── IDENTITY.md
│   │   └── skills/
│   ├── programmer/
│   │   ├── IDENTITY.md
│   │   └── skills/
│   └── reviewer/
│       ├── IDENTITY.md
│       └── skills/
├── tasks/
│   └── XENOS-001/
│       ├── 00-task-brief.md
│       ├── 01-orchestrator-brief.md
│       ├── 02-design/
│       ├── 03-implementation/
│       ├── 04-review/
│       └── 05-final/
├── shared/
│   ├── schemas/
│   └── templates/
└── archive/
```

## Setup

1. Create a private or public GitHub repository named `Xen-AI-Team`. Prefer private if task documents may contain proprietary source details.
2. Copy the contents of `github-template/` to the repository root.
3. Create four separate ChatGPT conversations.
4. In each conversation, paste the corresponding `agents/<role>/IDENTITY.md` and attach/paste the relevant skill files.
5. Keep each conversation dedicated to its role. Do not ask one role to impersonate another during normal workflow.
6. For each new project task, create a unique Task ID and task folder.
7. Pass handoffs manually between conversations using `shared/templates/handoff.md`.

## First message for each chat

After providing its identity and skill files, send:

> You are now operating as the Xen AI Team role defined in the provided identity and skills. Treat those documents as your operating contract. Confirm your role, authority limits, required inputs, output files, and handoff format. Do not begin a task until I provide a Task ID and task brief.

## Four chat identities

- Orchestrator: receives Director's request, clarifies requirements, creates task brief and delegation package. Does not approve its own plan.
- Designer: produces implementation-ready UI/UX and motion specifications. Does not implement app code.
- Programmer: implements only approved scope. Does not self-review or approve release.
- Reviewer: independently inspects supplied diff/files and evidence. Read-only; does not fix code.

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
