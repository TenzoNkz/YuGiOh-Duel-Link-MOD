# Mod Candidate Register

Status labels: NOT_INSPECTED, INDICATED_BY_STATIC_EVIDENCE, NEEDS_DEEPER_ANALYSIS, TESTED_IN_ISOLATED_ENVIRONMENT, NOT_SUPPORTED.

The current APK has not yet completed its automated static inventory. Until then, all candidates below are proposals, not findings.

| Candidate | Current status | Evidence needed | Scope |
|---|---|---|---|
| Existing AutoPlay Bot toggle | NOT_INSPECTED | Identify relevant code, callbacks, and prerequisites; do not infer function from label alone | Audit existing behavior |
| Show Monster & Status Details | NOT_INSPECTED | Determine where displayed values come from and whether the feature only changes local presentation | Prefer local visual analysis |
| Reveal Card Face | NOT_INSPECTED | Trace the feature and determine the source/availability of card information | Analyze visibility and data flow |
| Add a new menu toggle | NOT_INSPECTED | Identify the existing menu implementation, event wiring, and safe extension point | UI-only prototype may be possible |
| Visual/accessibility adjustments | NOT_INSPECTED | Find UI/resources and check whether changes remain local and compatible | Candidate for isolated testing |
| Offline damage-multiplier simulation | NOT_INSPECTED | Build a separate deterministic test model and verify its arithmetic with test cases | Offline simulation, not a live duel patch |
| Damage Multiplier affecting only the user's cards in online duels | NOT_INSPECTED | Static analysis cannot by itself prove server acceptance or safe feasibility | Do not implement a live-match cheat or claim it works |

## Per-candidate evidence template
For every candidate, record:
1. Exact APK and release tag analyzed.
2. File/class/method/resource evidence with names and line/address references where tooling permits.
3. What the evidence actually proves and what remains uncertain.
4. Dependencies, compatibility risks, crash risks, and whether the behavior appears local or server-authoritative.
5. Reproducible tests and outcomes.
6. Final status label and the reason for it.

No candidate may be marked as working based only on decompiled strings, menu labels, a successful build, or a speculative code path.
