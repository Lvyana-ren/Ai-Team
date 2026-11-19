# Skill: Independent Code Review

## Review procedure
1. Read approved brief, design/technical spec, and acceptance criteria.
2. Inspect diff against the correct base revision.
3. Trace changed code into relevant call sites and surrounding behavior.
4. Check failure paths, boundary conditions, concurrency, permissions, input validation, resource handling, and compatibility.
5. Compare test evidence with changed behavior.
6. Report only actionable findings, ordered by severity.
7. State what could not be verified.

## Severity
- BLOCKER: prevents release or causes catastrophic failure/data loss.
- CRITICAL: severe security, stability, or core functionality defect.
- HIGH: major acceptance failure or likely significant regression.
- MEDIUM: meaningful defect with narrower impact or missing validation.
- LOW: minor issue, maintainability concern, or edge case.

Do not inflate severity. Do not invent line numbers or test results.
