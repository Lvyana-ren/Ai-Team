# Skill: Implementation Engineering

## Procedure
1. Verify the approved brief and design/technical specification.
2. Inspect repository structure, conventions, relevant files, and current diff.
3. Propose a short implementation plan if changes are substantial.
4. Implement the smallest coherent change.
5. Add or update focused tests.
6. Run the narrowest tests first, then broader tests where practical.
7. Inspect the final diff for accidental or unrelated changes.
8. Write an evidence-based implementation report.

## Reporting format
For each command, record exact command, exit status, and meaningful output. Distinguish `PASSED`, `FAILED`, `NOT RUN`, and `BLOCKED`.

## Never
- Claim a build passed without running it.
- Guess missing APIs or file paths.
- Hide deviations from the specification.
- Include secrets in source, logs, or reports.
