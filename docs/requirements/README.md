# Padma SOS: Requirements

This folder takes Padma SOS from the problem down to testable requirements. Architecture (`docs/architecture/`) and the hardware/firmware design are derived from it.

```
problem → users → use cases → functional + non-functional requirements → architecture → HW / FW
```

| File | Contents |
|---|---|
| [01-problem-statement.md](01-problem-statement.md) | The problem, the target market, and why existing options fall short |
| [02-users-and-stakeholders.md](02-users-and-stakeholders.md) | Who wears it, who responds, and who else is affected |
| [03-use-cases.md](03-use-cases.md) | System context diagram, SOS flow, and use cases `UC-xx` |
| [04-functional-requirements.md](04-functional-requirements.md) | What the device must do (`FR-xxx`) |
| [05-non-functional.md](05-non-functional.md) | Size, battery, cost, robustness, privacy, regulatory (`NFR-xxx`) |
| [06-constraints-assumptions.md](06-constraints-assumptions.md) | Constraints, assumptions, open questions (`OQ-xx`) and risks |

## Conventions

- **IDs** are permanent. A dropped requirement is marked ~~struck through~~ with a reason; its ID is never reused.
- **Priority** (MoSCoW):
  - **M**: Must, the product is not viable without it
  - **S**: Should
  - **C**: Could, include it if size and cost allow
  - **W**: Won't (this version)
- **Trace:** every `FR`/`NFR` names the use case(s) it serves, so we can see what breaks when we cut something.
- **Status:** `draft` → `agreed` → `verified` (has a test).
- Diagrams use [Mermaid](https://mermaid.js.org/), which GitHub renders inline.
