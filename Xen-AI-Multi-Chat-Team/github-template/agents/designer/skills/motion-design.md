# Skill: Motion Design Specification

Describe motion as implementable behavior, not adjectives.

For each animation specify:
- Trigger and initial/final states
- Duration and delay in milliseconds
- Easing curve or named easing
- Translation, scale, rotation, opacity, and pivot as applicable
- Loop/repeat behavior
- Interruption and lifecycle behavior
- Reduced-motion fallback
- Performance constraints and expected frame rate

Avoid continuous animation when static feedback is sufficient. Prefer transform/opacity over layout-triggering properties where appropriate. Specify loading and error behavior as well as the ideal path.
