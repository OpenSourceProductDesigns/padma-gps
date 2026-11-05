# Padma SOS: Architecture

Status: `draft`

This folder turns the requirements in [`docs/requirements/`](../requirements/README.md) into a system design. It goes top-down: the whole device first, then each subsystem.

```
requirements → system block diagram → power budget → subsystem design → HW schematic / FW modules
```

| File | Contents |
|---|---|
| [01-system-block-diagram.md](01-system-block-diagram.md) | Blocks, interfaces, power rails, SOS timeline, architecture decisions `AD-xx`, candidate parts |
| [02-power-budget.md](02-power-budget.md) | Standby and SOS current estimates, battery life by modem idle strategy, SOS reserve, peak current |
| [03-lte-module-selection.md](03-lte-module-selection.md) | LTE Cat 1 bis module shortlist for India: VoLTE, PCM audio, size, power, open vendor questions |

## Conventions

- **Architecture decisions** have permanent IDs `AD-xx`. Each one names the requirements it serves and has a status: `proposed` → `agreed` → `superseded`.
- Part numbers are **examples to evaluate**, not selections. Every number taken from a datasheet still has to be checked against the actual part.
- Estimates are written as **low / typical / high** so we can see which assumptions matter most.
