# Xen AI Team

**A manually coordinated, role-based multi-chat workflow for planning, designing, implementing, and independently reviewing software work.**

> **Operating model:** Four dedicated ChatGPT conversations, one human Director, and one GitHub repository as the shared source of truth. Handoffs between chats are manual.

- **Director:** human owner, scope authority, and final acceptance decision.
- **XEN-ORCHESTRATOR:** planning, decomposition, dependency management, and handoff preparation.
- **XEN-DESIGNER:** UI/UX and interaction specifications.
- **XEN-PROGRAMMER:** approved implementation and validation.
- **XEN-REVIEWER:** independent, read-only review.

This README is the operational entry point. The detailed rules remain in the linked policy, identity, skill, schema, and template files. When in doubt, read those source documents rather than relying on a summary in this README.

---

## Contents

1. [What this repository is](#what-this-repository-is)
2. [How the system works](#how-the-system-works)
3. [Repository structure](#repository-structure)
4. [Prerequisites](#prerequisites)
5. [Initial setup](#initial-setup)
6. [Preparing each ChatGPT role](#preparing-each-chatgpt-role)
7. [Starting a task](#starting-a-task)
8. [End-to-end task lifecycle](#end-to-end-task-lifecycle)
9. [Handoff protocol](#handoff-protocol)
10. [Skills and preflight enforcement](#skills-and-preflight-enforcement)
11. [Testing and verification](#testing-and-verification)
12. [Workflow states and review verdicts](#workflow-states-and-review-verdicts)
13. [Artifacts, manifests, and evidence](#artifacts-manifests-and-evidence)
14. [Git and branch workflow](#git-and-branch-workflow)
15. [Security and authority boundaries](#security-and-authority-boundaries)
16. [Troubleshooting](#troubleshooting)
17. [Operational checklists](#operational-checklists)
18. [Reference documents](#reference-documents)

---

## What this repository is

Xen AI Team is an operating framework for coordinating four separate ChatGPT conversations. Each conversation has a narrowly defined role, responsibilities, required outputs, skill catalog, and authority limits.

The repository provides:

- Role contracts in `agents/<role>/IDENTITY.md`.
- Role-specific skill catalogs and curated upstream skill libraries.
- Shared task, handoff, and artifact templates.
- JSON Schemas for validating handoff and artifact-manifest structure.
- A common handoff protocol and skill-enforcement policy.
- A durable record of task briefs, deliverables, evidence, decisions, and review outcomes.

### What it is not

This repository does **not** create an autonomous multi-agent runtime.

Separate ChatGPT conversations do not automatically:

- Read one another's chat history.
- Send messages to one another.
- Delegate tasks to another conversation.
- Run continuously in the background.
- Know that another role has finished.
- Synchronize their local context automatically.

The **Director manually relays** the approved brief, handoff, and required artifacts from one conversation to the next. GitHub is the shared record, not a message bus.

A role may inspect or modify GitHub only when that conversation has an authorized connection/tool and the required permission. If it does not, the Director must provide the files by upload or paste. A filename or path alone is not proof that a role accessed the file.

---

## How the system works

The normal control flow is:

```text
                 DIRECTOR
        (goal, scope, approval, acceptance)
                     |
                     v
              XEN-ORCHESTRATOR
       clarify -> research -> plan -> split
                     |
          +----------+----------+
          |                     |
          v                     v
     XEN-DESIGNER          XEN-PROGRAMMER
   design specification   implementation
          |                     |
          +----------+----------+
                     |
          approved inputs / handoff
                     |
                     v
              XEN-PROGRAMMER
             build + test + report
                     |
                     v
               XEN-REVIEWER
          independent read-only review
                     |
                     v
                 DIRECTOR
          accept / request changes / stop
                     |
             explicit release approval
```

The diagram is a conceptual route, not a requirement that every task use all four roles. A documentation-only or narrowly scoped task may need fewer roles. The Orchestrator must explain which roles are needed and why.

### Core operating sequence

Every role follows this discipline:

1. **IDENTITY** — read and obey the complete role contract.
2. **SKILL INDEX** — inspect the role's skill catalog.
3. **SKILL PREFLIGHT** — select and read applicable full skills and required local references.
4. **TASK EXECUTION** — work only within the assigned scope and authority.
5. **REPORT** — state deliverables, evidence, checks, blockers, and limitations.
6. **HANDOFF** — prepare the next transfer using the shared protocol/template.

The sequence is mandatory. Do not skip preflight because a task looks easy.

---

## Repository structure

The following is the intended high-level layout. Some folders contain role-specific upstream skill snapshots and task records beyond this abbreviated view.

```text
Xen-AI-Team/
├── README.md
├── HANDOFF-PROTOCOL.md
├── THIRD-PARTY-SKILLS.md
├── director/
├── agents/
│   ├── orchestrator/
│   │   ├── IDENTITY.md
│   │   └── skills/
│   │       ├── SKILL-INDEX.md
│   │       └── upstream/
│   │
│   ├── designer/
│   │   ├── IDENTITY.md
│   │   └── skills/
│   │       ├── SKILL-INDEX.md
│   │       └── upstream/
│   │
│   ├── programmer/
│   │   ├── IDENTITY.md
│   │   └── skills/
│   │       ├── SKILL-INDEX.md
│   │       └── upstream/
│   │
│   └── reviewer/
│       ├── IDENTITY.md
│       └── skills/
│           ├── SKILL-INDEX.md
│           └── upstream/
│
├── tasks/
│   └── <TASK-ID>/
│       ├── task-brief.md
│       ├── task-status.json
│       ├── artifact-manifest.json
│       ├── handoffs/
│       ├── design/
│       ├── implementation/
│       ├── review/
│       └── evidence/
│
├── shared/
│   ├── SKILL-ENFORCEMENT.md
│   ├── SKILL-DEPENDENCIES.md
│   ├── schemas/
│   │   ├── handoff.schema.json
│   │   └── artifact-manifest.schema.json
│   └── templates/
│       ├── task-brief.md
│       ├── handoff.md
│       └── task-status.json
│
└── archive/
```

The `tasks/<TASK-ID>/` layout above is a recommended per-task organization convention. Create only the subdirectories needed by that task; do not assume every example folder already exists.

### Directory responsibilities

| Path | Purpose |
|---|---|
| `director/` | Director-facing planning notes, operating decisions, or materials maintained for the project |
| `agents/<role>/IDENTITY.md` | Role mission, authority, responsibilities, prohibitions, and mandatory preflight |
| `agents/<role>/skills/SKILL-INDEX.md` | Skills available to that role and their task triggers |
| `agents/<role>/skills/upstream/` | Vendored skill source snapshots; preserve upstream attribution |
| `tasks/<TASK-ID>/` | Durable record for one task |
| `shared/schemas/` | Machine-readable structure contracts |
| `shared/templates/` | Starting templates for briefs, handoffs, and status |
| `archive/` | Superseded or closed historical material, retained when useful |

---

## Prerequisites

### Required for the basic workflow

- A GitHub account with access to this repository.
- Four separate ChatGPT conversations, one for each role.
- A human Director who can relay documents and make approval decisions.
- A way to read the repository files in each conversation: authorized GitHub access, or manual upload/paste.
- A task folder and the shared templates for each tracked task.

### Required only when the selected task needs them

Tools are task-dependent. Do not assume that every role or every chat has every tool.

| Prerequisite | Typical task |
|---|---|
| GitHub read access | Inspect repository files, branches, commits, diffs, and PRs |
| GitHub write access | Create or update files/branches/PRs when explicitly authorized |
| Python 3 | Skills, scripts, JSON checks, or data processing that require Python |
| JSON Schema validator | Validate handoff and artifact manifest against their schemas |
| JDK + Kotlin compiler | Kotlin/JVM compilation and tests |
| Gradle | Android/JVM Gradle build and test tasks |
| Android SDK/build tools | Android build, lint, packaging, and device tooling |
| Android device/emulator | UI, integration, compatibility, and runtime validation |
| Kernel toolchain | Kernel build, image packaging, and static checks |
| Device recovery/flash access | Flash and boot validation; always requires explicit Director approval |

Record each relevant prerequisite in the task's environment/prerequisite inventory using one of these exact states:

- `available` — checked and usable in the current environment.
- `unavailable` — checked and missing, inaccessible, or unusable.
- `not_applicable` — not required by the selected procedure.
- `not_checked` — not verified; availability must not be assumed.

See [shared/SKILL-DEPENDENCIES.md](shared/SKILL-DEPENDENCIES.md).

---

## Initial setup

### 1. Obtain the repository

Clone the repository to a trusted workspace:

```bash
git clone https://github.com/Lvyana-ren/Xen-AI-Team.git
cd Xen-AI-Team
git switch main
git pull --ff-only origin main
```

If the repository is private, authenticate through your normal GitHub credential manager or approved SSH setup. Never put a personal access token directly into a command, source file, task brief, or chat message.

### 2. Inspect the operating documents

Before creating the role conversations, read these files in order:

1. `README.md` — this overview and setup guide.
2. `HANDOFF-PROTOCOL.md` — task transfer and revision rules.
3. `shared/SKILL-ENFORCEMENT.md` — mandatory skill preflight and partial-execution rules.
4. `shared/SKILL-DEPENDENCIES.md` — environment prerequisite inventory.
5. The four role `IDENTITY.md` files.
6. The four role `skills/SKILL-INDEX.md` files.
7. The shared templates and schemas.

Do not assume this README replaces the complete role contracts or skill instructions.

### 3. Create the four dedicated conversations

Create one conversation for each role:

- `XEN-ORCHESTRATOR`
- `XEN-DESIGNER`
- `XEN-PROGRAMMER`
- `XEN-REVIEWER`

Keep each conversation dedicated to its assigned role. Do not use one chat as multiple roles for convenience; role separation is part of the review and authority model.

### 4. Load each role's documents

For each conversation, provide:

1. Its complete `agents/<role>/IDENTITY.md`.
2. Its complete `agents/<role>/skills/SKILL-INDEX.md`.
3. The full `SKILL.md` of every skill required or selected for the current task.
4. Any local references, examples, scripts, or data explicitly required by those skills.
5. The current task brief and handoff when a task is assigned.

You can provide these using an authorized repository connection, file upload, or pasted content. If a role cannot access a referenced file, it must report the missing path. Do not treat a link or filename as proof of a successful read.

### 5. Initialize the role

After loading the role documents, send this initialization instruction:

> You are now operating as the Xen AI Team role defined in the provided identity and skills. Treat those documents as your operating contract. Confirm your role, authority limits, required inputs, output files, and handoff format. Do not begin a task until I provide a Task ID and task brief.

The role should confirm its identity and constraints. This is an initialization check, not proof that it can successfully perform every future task.

### 6. Confirm repository access and permissions

For each conversation, establish what it can actually do:

- Can it read the target repository?
- Can it inspect the required branch and files?
- Can it inspect diffs and commits?
- Can it create a branch or update files, if that is part of an approved task?
- Does it have read-only or write access?

Report actual access. Never infer write permission from read permission. The Reviewer should receive only the minimum material needed and should remain read-only.

---

## Preparing each ChatGPT role

| Role | Primary responsibility | Expected output | Must not |
|---|---|---|---|
| Orchestrator | Clarify, research, decompose, sequence, and prepare delegation packages | Task brief, work breakdown, assignment/dependency plan, risk/prerequisite register, next handoff | Implement project source, approve work, or claim it contacted another chat |
| Designer | Convert approved product requirements into implementable design specifications | User flows, screen/component specs, design tokens, interaction/motion rules, accessibility and edge states | Implement app code or authorize implementation/release |
| Programmer | Implement approved scope and provide reproducible validation evidence | Source changes, tests, build/test report, diff, Reviewer handoff | Expand scope, self-approve, or perform unauthorized release/flash |
| Reviewer | Independently compare the candidate against approved scope and evidence | Review report, findings, acceptance matrix, residual risks, recommendation | Edit/fix code, rely only on Programmer's self-review, or authorize release |

### Role-specific setup notes

**Orchestrator**
- Required every task: `plan-orchestrate` and `search-first`.
- For multi-stage work, include work-item IDs, owner assignments, dependencies, parallel lanes, acceptance criteria, risks, prerequisites, and manual handoff order.
- It prepares the delegation package; the Director performs the actual relay.

**Designer**
- Required every UI task: `ui-ux-pro-max`.
- Add motion, native mobile, Compose, or animation skills only when their triggers apply.
- Do not apply Jetpack Compose guidance to a Views-based UI or another toolkit.
- For the vendored UI/UX Pro Max CLI, follow its own `SKILL.md`; set `XEN_AI_TEAM_ROOT` to the repository root and verify Python 3 before claiming the CLI ran.

**Programmer**
- Required every implementation: `implement`, `coding-standards`, and `verification-loop`.
- Select TDD, bug diagnosis, Kotlin, Gradle, Compose, benchmarking, or Android/kernel specialist skills when relevant.
- Read the full procedure and its referenced examples before using it.

**Reviewer**
- Required every review: `code-review`, `verification-loop`, and `change-impact`.
- Add security, performance, benchmark, Android, UI-test, or concurrency skills when relevant.
- Review the actual baseline and candidate, not just a summary of what changed.

The exact paths and current required skills are defined in each role's `SKILL-INDEX.md`. The index is authoritative for skill selection; this README is only a quick reference.

---

## Starting a task

### 1. Assign a unique Task ID

Use the format:

```text
PROJECT-001
PROJECT-002
PROJECT-003
```

The schema requires an uppercase alphanumeric project prefix followed by a hyphen and at least three digits. Example: `XENOS-001`.

Do not reuse a Task ID for unrelated work. Keep follow-up changes under the same Task ID only when they are part of the same approved scope.

### 2. Create the task folder

Create `tasks/<TASK-ID>/` and copy the relevant shared templates:

- `shared/templates/task-brief.md` → `tasks/<TASK-ID>/task-brief.md`
- `shared/templates/task-status.json` → `tasks/<TASK-ID>/task-status.json`
- Create `tasks/<TASK-ID>/artifact-manifest.json` using `shared/schemas/artifact-manifest.schema.json` as its structure contract.

Create `handoffs/`, `evidence/`, `design/`, `implementation/`, and `review/` only as needed.

### 3. Fill the task brief

At minimum, specify:

- Task ID and title.
- Target repository and branch.
- Platform, device, API, OS, or kernel version where relevant.
- Baseline revision and candidate revision when available.
- Goal and current behavior.
- Expected behavior.
- In-scope and out-of-scope work.
- Constraints and known risks.
- Work breakdown and dependencies.
- Acceptance criteria.
- Validation plan.
- Required approvals.

The Orchestrator may clarify missing requirements, but it must not silently decide unresolved product or technical trade-offs for the Director.

### 4. Approve the scope

The Director reviews the task brief and explicitly approves the scope before implementation begins. A draft brief is not implementation authorization.

---

## End-to-end task lifecycle

### Stage A — Director opens the task

1. Director creates the Task ID and task folder.
2. Director provides the Orchestrator with the task goal, context, constraints, and relevant source material.
3. Orchestrator verifies inputs and performs its mandatory skill preflight.
4. Orchestrator asks concise clarifying questions if an essential requirement is missing.

**Output:** a task brief and an orchestration/delegation plan.

### Stage B — Orchestrator plans the work

For a multi-agent or multi-stage task, the Orchestrator prepares:

1. Work breakdown structure with unique work-item IDs.
2. Agent assignment matrix: role, deliverable, and authority boundary.
3. Dependency graph/order, including safe parallel lanes and blocking dependencies.
4. Acceptance criteria for each work item.
5. Risk register and environment-prerequisite inventory.
6. Manual handoff sequence and Director approval gates.
7. Ready-to-send handoff packages for the next role(s).

It must distinguish a proposed assignment from an actual handoff. Listing a role in a plan does not mean that role has received or started the task.

**Director gate:** review and approve the task scope and plan before downstream work.

### Stage C — Designer prepares the specification (when needed)

1. Director manually passes the approved brief and required inputs to XEN-DESIGNER.
2. Designer verifies task ID, version, approval, and artifact access.
3. Designer performs skill preflight.
4. Designer inspects existing product conventions and supplied assets.
5. Designer creates implementation-ready specifications and objective acceptance criteria.
6. Designer returns the deliverables and Programmer handoff.

If the task does not involve design, the Orchestrator should explain why the Designer stage is not applicable.

**Director gate:** approve the design/technical specification before implementation when the task requires it.

### Stage D — Programmer implements

1. Director manually passes the approved brief, specifications, and required source artifacts to XEN-PROGRAMMER.
2. Programmer verifies the handoff and confirms target repository/branch and baseline revision.
3. Programmer performs skill preflight and checks runtime prerequisites.
4. Programmer inspects the existing codebase before editing.
5. Programmer implements only the approved scope.
6. Programmer adds or updates relevant tests.
7. Programmer runs available validation checks and records exact commands and results.
8. Programmer inspects the final diff for unintended changes and security issues.
9. Programmer prepares the implementation report, candidate artifacts, evidence, manifest updates, and Reviewer handoff.

A Programmer report of `completed` means only that its assigned work is complete. It is not independent review, Director acceptance, or release approval.

### Stage E — Reviewer independently audits

1. Director manually passes the approved scope, baseline, candidate diff/files, Programmer report, and evidence to XEN-REVIEWER.
2. Reviewer verifies task identity, approved scope, versions, and artifact access.
3. Reviewer performs its own skill preflight.
4. Reviewer inspects the actual changes and relevant surrounding code.
5. Reviewer checks acceptance criteria, test adequacy, security, compatibility, regression risk, and claims made in the report.
6. Reviewer reproduces checks where tools and environment permit.
7. Reviewer records findings with severity, location, evidence, impact, and remediation guidance.
8. Reviewer returns an independent report and recommendation.

Reviewer is read-only. It does not fix the implementation or directly authorize Programmer changes.

### Stage F — Director decides

The Director considers the review report and chooses the next action:

- Accept the result.
- Request a scoped revision.
- Ask for additional evidence or testing.
- Reject the candidate.
- Stop or defer the task.

For a revision, the Director reviews the findings and explicitly authorizes the scope of changes. The Programmer revises, then the Reviewer rechecks. After three unsuccessful review cycles, stop and ask the Director for a recovery decision.

### Stage G — Close or release

1. Record the final review outcome and Director decision.
2. Update task status and artifact manifest.
3. Preserve the final accepted artifacts and evidence.
4. Mark superseded handoffs/artifacts when newer versions replace them.
5. Merge, publish, deploy, release, or flash only after explicit Director authorization.

---

## Handoff protocol

Handoffs are manual and must be explicit.

### Standard transfer

1. Sending role creates a handoff document using `shared/templates/handoff.md`.
2. Sending role identifies every deliverable and its exact repository path.
3. Sending role updates the task artifact manifest when files are created or transferred.
4. Director saves the handoff and artifacts to the task folder.
5. Director opens the recipient conversation and supplies the handoff plus referenced files.
6. Recipient verifies task ID, version, sender, recipient, approvals, required inputs, and artifact integrity where hashes are provided.
7. Recipient reports which artifacts it could actually access.
8. Recipient performs only its assigned role and returns its own handoff.

### Handoff versioning

Use:

```text
<TASK-ID>-<ROLE>-v<MAJOR.MINOR>
```

Example:

```text
XENOS-001-ORCHESTRATOR-v1.0
XENOS-001-DESIGNER-v1.0
XENOS-001-PROGRAMMER-v1.0
XENOS-001-REVIEWER-v1.0
```

If an upstream brief or specification changes, downstream work based on the old version may be stale. Mark the old handoff `superseded` and request a new handoff. Do not silently continue against conflicting versions.

### Recipient acceptance checklist

Before starting, the receiving role confirms:

- [ ] Task ID matches.
- [ ] Handoff version is the latest known version.
- [ ] Sender and recipient are correct.
- [ ] Required documents are present and readable.
- [ ] Artifact references resolve and hashes match when supplied.
- [ ] Required Director approval exists.
- [ ] Scope and acceptance criteria are unambiguous.
- [ ] Required skills and environment prerequisites are identified.

If a required item is missing or inconsistent, block the affected work and identify the exact issue. Independent authorized checks may continue if they do not depend on the blocker.

See [HANDOFF-PROTOCOL.md](HANDOFF-PROTOCOL.md) for the complete rules and manual relay prompt.

---

## Skills and preflight enforcement

Skills are procedural instructions, not merely reference titles.

### Required preflight

Before task execution, every role must:

1. Read its complete `IDENTITY.md`.
2. Read its `skills/SKILL-INDEX.md`.
3. Select all applicable required/specialist skills.
4. Read each selected skill's complete `SKILL.md`.
5. Read local references/examples required by that skill's procedure.
6. Inspect/use supporting scripts or data when explicitly required and available.
7. Record exact paths read, applicability, and concrete steps applied.

A skill title, directory listing, or remembered description does not count as reading the full skill.

### Missing skill versus missing tool

These are different blockers:

- **Missing skill:** stop the affected procedure with `BLOCKED_SKILL_UNAVAILABLE`. Identify the missing path. Do not invent its contents or silently replace it with general knowledge.
- **Missing environment prerequisite:** record the prerequisite as `unavailable`; block only the procedure/check that requires it. Do not claim it ran.

Continue independent, authorized checks that do not depend on the missing skill or prerequisite. For example, an unavailable Gradle installation may block a Gradle build but not necessarily source inspection or review of supplied test files.

### Skill Usage Record

Every completion report/handoff must include a Skill Usage Record with:

| Field | Meaning |
|---|---|
| Skill | Exact skill name |
| Path | Exact repository path read |
| Applicability | Why it applies to this task |
| Procedure applied | Concrete step(s) actually used |
| Result | Artifact, decision, test, or finding produced |

Never claim a skill was read or used unless it was actually inspected and applied.

**Enforcement limitation:** these are auditable procedural gates. Markdown alone cannot technically prevent a model from ignoring instructions. A future runtime can strengthen enforcement with pre-task hooks or automated validation.

See [shared/SKILL-ENFORCEMENT.md](shared/SKILL-ENFORCEMENT.md).

---

## Testing and verification

Testing must be planned from the acceptance criteria, not added as an afterthought. The exact test strategy depends on the task, selected skills, codebase, and available environment.

### 1. Define acceptance criteria first

Each criterion should be observable and testable. Avoid statements such as "works correctly" without defining the expected behavior and how it will be checked.

A useful validation matrix:

| ID | Requirement / acceptance criterion | Validation method | Expected result | Evidence |
|---|---|---|---|---|
| AC-01 | Defined behavior | Unit / static / manual / device test | Explicit expected outcome | Log, test report, screenshot, or trace |
| AC-02 | Compatibility constraint | Build / integration / device test | Supported target passes | Build output or device record |
| AC-03 | Regression constraint | Regression test / comparison | No defined regression | Before/after evidence |

### 2. Separate validation levels

Report each level separately. Passing one level does not imply that later levels passed.

| Level | What it establishes | Example evidence |
|---|---|---|
| Document/schema validation | Required fields and structure are valid | JSON parser or JSON Schema validator output |
| Static inspection | Source/configuration was inspected without executing it | File/line references, static analysis report |
| Compilation/build | Candidate compiles or packages in the stated environment | Exact command, tool versions, exit code, build log |
| Unit tests | Isolated logic passes its tests | Test command, test count, pass/fail output |
| Integration tests | Components work together at the tested boundary | Test report, logs, reproducible setup |
| UI/E2E tests | User flows behave as specified | Test run, screenshots/video, device/emulator details |
| Device/runtime validation | Behavior was observed on the named target | Device model, OS/build, steps, logs |
| Performance/benchmark validation | A measured result under stated conditions | Tool/version, workload, temperature, power state, repetitions, raw results |
| Release validation | Final packaged candidate and release procedure were checked | Artifact hash, signing/package checks, approved release record |

Do not label static inspection as a test run. Do not claim device compatibility from a successful compile. Do not claim performance improvement from a single uncontrolled measurement.

### 3. Run only checks supported by the current environment

Before running a check:

1. Confirm the relevant skill has been read.
2. Check the required tool/runtime/device access.
3. Record versions and environment details.
4. Use the exact command or procedure required by the skill.
5. Save the relevant output as evidence.
6. Report failures and limitations honestly.

If a test cannot run, mark it `blocked` or `not_run` as appropriate and explain why. Never fabricate a passing result to complete a checklist.

### 4. Record exact test commands and outcomes

A useful report entry:

```text
Check: Kotlin unit tests
Status: passed
Environment: Kotlin <version>, JDK <version>
Command: <exact command>
Result: <actual test count and pass/fail summary>
Evidence: tasks/<TASK-ID>/evidence/<file>
Limitations: <what this does not establish>
```

For a failed or unavailable check, retain the actual error or explain why it was not run.

### 5. Programmer and Reviewer have different jobs

- Programmer adds/runs relevant tests and reports implementation evidence.
- Reviewer independently inspects the candidate and evidence, and reproduces checks where possible.
- Reviewer must not accept a claim solely because Programmer wrote it in a report.
- Director decides whether the reviewed result is accepted.

### 6. Validate repository metadata

The repository includes JSON Schemas for handoff and artifact manifests. At minimum, parse JSON files before submitting changes:

```bash
python3 -m json.tool shared/schemas/handoff.schema.json >/dev/null
python3 -m json.tool shared/schemas/artifact-manifest.schema.json >/dev/null
python3 -m json.tool tasks/<TASK-ID>/task-status.json >/dev/null
python3 -m json.tool tasks/<TASK-ID>/artifact-manifest.json >/dev/null
```

JSON parsing checks syntax only. It does **not** prove conformance to the JSON Schema.

If Python's `jsonschema` package is installed, validate an instance against its schema:

```bash
python3 -m jsonschema -i tasks/<TASK-ID>/artifact-manifest.json shared/schemas/artifact-manifest.schema.json
```

Use the validator's documented CLI syntax/version in the actual environment. Record the package/version and command. If the validator is unavailable, report schema validation as `not_run`; do not equate a successful JSON parse with schema validation.

The handoff schema can be validated the same way against a completed handoff JSON file, if the task maintains one.

### 7. Final diff and review checks

Before handing implementation to Reviewer, Programmer should inspect:

```bash
git status --short
git diff --check
git diff --stat
git diff
```

These commands help identify whitespace errors and unintended changes; they do not replace compilation, tests, or independent review.

Reviewer should compare the approved baseline and candidate revisions and verify each acceptance criterion against actual artifacts/evidence.

---

## Workflow states and review verdicts

Workflow status and review verdict are separate concepts.

### Workflow status

| Status | Meaning |
|---|---|
| `draft` | Being prepared; not ready for downstream execution |
| `ready` | Required inputs and approvals for the next stage are present |
| `in_progress` | Authorized work is underway |
| `blocked` | The next required action cannot proceed |
| `needs_changes` | A required correction is outstanding |
| `completed` | Assigned work is complete; not Director acceptance or release approval |
| `superseded` | Replaced by a newer task/handoff version |

### Review verdict

The handoff schema reserves these values for an independent review outcome:

| Verdict | Meaning |
|---|---|
| `pass` | Reviewed against scope and acceptance criteria; no blocking findings |
| `pass_with_observations` | Pass with documented non-blocking observations |
| `conditional_pass` | Acceptance depends on explicitly stated conditions |
| `reject` | Material findings prevent acceptance |
| `insufficient_evidence` | Review attempted but evidence is inadequate |
| `not_reviewed` | No independent review was performed |

Do not put a review verdict in the workflow `status` field. A Programmer may report `completed`; only the Reviewer supplies an independent review verdict; only the Director accepts the final result.

The canonical field definitions and allowed values are in [shared/schemas/handoff.schema.json](shared/schemas/handoff.schema.json).

---

## Artifacts, manifests, and evidence

### Why the manifest exists

The artifact manifest tracks the provenance and integrity of files exchanged during a task. It helps the receiving role distinguish:

- Original input.
- Baseline version.
- Candidate output.
- Supporting evidence.
- Report.
- Other task material.

Each manifest artifact records:

- `artifact_id`
- `path`
- `role`
- `version`
- `sha256`
- `size_bytes`
- `media_type`
- `source`
- `parent_artifact_id`
- `verification`
- `notes`

The allowed structure is defined by [shared/schemas/artifact-manifest.schema.json](shared/schemas/artifact-manifest.schema.json).

### Hash and verification discipline

- Compute SHA-256 from the actual file bytes.
- Do not copy a hash from a filename or guess it.
- Recompute the hash after modifying an artifact.
- A matching hash establishes byte identity, not correctness.
- Record the actual verification level: `not_checked`, `hash_verified`, `content_inspected`, or `independently_reproduced`.
- Do not mark an artifact independently reproduced unless another party actually reproduced the relevant result.

### Evidence should be minimal but sufficient

Include only evidence relevant to the task and acceptance criteria. Redact secrets, personal data, tokens, and unrelated private logs before storing or transferring evidence.

---

## Git and branch workflow

The repository is the shared source of truth. Use a clear, reviewable Git history.

### Recommended workflow

1. Update local `main`.
2. Create a task/documentation branch from the current `main`.
3. Make only the approved changes.
4. Inspect the diff and validate affected files.
5. Push the branch only when authorized and permitted.
6. Open a pull request targeting `main`.
7. Review the PR and its evidence.
8. Merge only after explicit Director approval.
9. Confirm the resulting `main` commit and record it in the task.

Example:

```bash
git switch main
git pull --ff-only origin main
git switch -c docs/<short-description>

# Make the approved changes.

git status --short
git diff --check
git diff

git add <approved-paths>
git commit -m "docs(<TASK-ID>): describe the change"
```

If the task requires pushing and the Director has authorized it:

```bash
git push -u origin docs/<short-description>
```

Do not force-push, rewrite shared history, or merge without explicit authorization.

### Commit message examples

```text
docs(XENOS-001): add task operating guide
design(XENOS-002): add dashboard interaction specification
feat(XENOS-003): implement approved settings screen
test(XENOS-003): add settings regression tests
review(XENOS-003): add independent review report
```

Use the convention in [HANDOFF-PROTOCOL.md](HANDOFF-PROTOCOL.md) and keep commits focused.

---

## Security and authority boundaries

These rules apply to every role and every task:

- Never commit API keys, passwords, private keys, signing keys, tokens, or personal data.
- Redact secrets from logs, screenshots, build output, and handoffs.
- Do not run destructive commands or flash devices based on a chat instruction alone.
- Do not push, merge, publish, deploy, release, or flash without explicit Director approval.
- Do not treat tool availability as permission to use it.
- Do not expand approved scope silently.
- Do not claim a repository was read, changed, tested, or verified unless that action actually occurred.
- Do not expose unrelated source files or private logs to Reviewer.
- Reviewer remains read-only and cannot approve release.
- The Orchestrator cannot approve its own plan.
- Programmer cannot self-approve implementation.
- A completed task is not automatically accepted.

If instructions, task documents, versions, or approvals conflict, stop the affected work and ask the Director. Do not silently reconcile conflicting instructions.

### Source-of-truth priority

1. Explicit latest Director decision for the Task ID.
2. Approved task brief and approved design/technical specification.
3. Latest versioned handoff document.
4. Repository source and test evidence.
5. Chat conversation context.

---

## Troubleshooting

| Problem | Correct response |
|---|---|
| Role cannot read its IDENTITY or skill index | Stop task execution and request the missing file |
| Required skill path is missing | Report `BLOCKED_SKILL_UNAVAILABLE`; do not substitute memory |
| Skill exists but required runtime/tool is missing | Mark that prerequisite `unavailable`; block only dependent checks |
| GitHub repository is inaccessible | Ask Director to provide the required files or authorize a suitable connection |
| Handoff points to a missing file | Mark the affected work blocked and identify the unresolved path |
| Artifact hash does not match | Do not consume it as the expected artifact; request a verified copy |
| Task ID or handoff version conflicts | Stop and ask Director which version is authoritative |
| Scope is ambiguous or has expanded | Ask Director for a decision before implementing the disputed scope |
| Build succeeds but tests cannot run | Report build and tests separately; tests remain `not_run` or `blocked` |
| Unit tests pass but device is unavailable | Report unit-test evidence only; do not claim device/runtime compatibility |
| Reviewer finds defects | Director reviews findings and authorizes any revision |
| Three review cycles fail | Stop and request a Director recovery decision |
| Chat claims another agent has completed work | Require the actual handoff and artifacts; chats do not auto-communicate |

---

## Operational checklists

### Director — before starting

- [ ] Assign a unique Task ID.
- [ ] Create the task folder and copy the templates.
- [ ] Provide complete context and source material.
- [ ] Obtain Orchestrator plan where task complexity requires it.
- [ ] Approve scope, constraints, and acceptance criteria.
- [ ] Approve design/technical specification before implementation when applicable.

### Every role — before execution

- [ ] Read complete role IDENTITY.
- [ ] Read role SKILL-INDEX.
- [ ] Read all selected full SKILL.md files and required references.
- [ ] Record exact skill paths and why they apply.
- [ ] Check environment prerequisites.
- [ ] Verify task ID, handoff version, scope, and approval.
- [ ] Confirm actual access to referenced artifacts.

### Programmer — before Reviewer handoff

- [ ] Changes stay within approved scope.
- [ ] Relevant tests were added/updated where appropriate.
- [ ] Exact commands, tool versions, and outcomes are recorded.
- [ ] Failed, blocked, and unrun checks are clearly distinguished.
- [ ] Final diff was inspected.
- [ ] Candidate artifacts and evidence are saved.
- [ ] Artifact manifest is updated.
- [ ] Reviewer handoff is complete.

### Reviewer — before final recommendation

- [ ] Baseline and candidate are identified.
- [ ] Actual diff and relevant source were inspected.
- [ ] Acceptance criteria were checked individually.
- [ ] Test evidence was inspected or independently reproduced where possible.
- [ ] Findings include severity, location, evidence, and impact.
- [ ] Unverified areas and residual risks are listed.
- [ ] Review verdict is separate from workflow status.
- [ ] No code was modified.

### Director — before acceptance or release

- [ ] Review report and findings were considered.
- [ ] Required corrections and conditions are resolved.
- [ ] Final artifacts and evidence are identifiable.
- [ ] Task status and manifest are current.
- [ ] Acceptance is explicitly recorded.
- [ ] Separate release/merge/deploy/flash approval is given if required.

---

## Reference documents

| Document | Why you need it |
|---|---|
| [HANDOFF-PROTOCOL.md](HANDOFF-PROTOCOL.md) | Full manual transfer rules, versioning, dependency-aware orchestration, revision loop, and relay prompt |
| [shared/SKILL-ENFORCEMENT.md](shared/SKILL-ENFORCEMENT.md) | Mandatory preflight, missing-skill/prerequisite handling, partial execution, and reporting |
| [shared/SKILL-DEPENDENCIES.md](shared/SKILL-DEPENDENCIES.md) | Environment prerequisite statuses and task inventory |
| [shared/schemas/handoff.schema.json](shared/schemas/handoff.schema.json) | Handoff JSON structure and allowed field values |
| [shared/schemas/artifact-manifest.schema.json](shared/schemas/artifact-manifest.schema.json) | Artifact provenance and integrity structure |
| [shared/templates/task-brief.md](shared/templates/task-brief.md) | New task specification template |
| [shared/templates/handoff.md](shared/templates/handoff.md) | Standard role-to-role handoff template |
| [shared/templates/task-status.json](shared/templates/task-status.json) | Initial task status template |
| [THIRD-PARTY-SKILLS.md](THIRD-PARTY-SKILLS.md) | Upstream skill provenance and attribution |
| `agents/<role>/IDENTITY.md` | Role-specific authority and responsibilities |
| `agents/<role>/skills/SKILL-INDEX.md` | Role-specific skill selection and required skills |

---

## Final operating principle

**The Director controls decisions. The Orchestrator controls planning. The Designer controls design specifications. The Programmer controls implementation within approved scope. The Reviewer controls independent assessment. GitHub preserves the evidence and shared record.**

No role may take over another role's authority, and no task is accepted merely because a chat says it is finished.
