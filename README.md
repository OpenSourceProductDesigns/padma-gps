# Padma GPS

**Padma GPS** is an ultra-compact, open-source GPS tracker designed as a base platform for **women's personal safety devices**: SOS alerts, live location sharing, and wearable or keychain form factors.

Everything is open: schematics, PCB layout, BOM, firmware, enclosure, and documentation. Anyone can study, build, and improve it.

Part of [OpenSourceProductDesigns](https://github.com/OpenSourceProductDesigns). Designed in [KiCad](https://www.kicad.org/).

> **Status:** 🚧 Early design, not yet functional.

> ⚠️ **Safety disclaimer:** Padma GPS is an open hardware project and is **not a certified safety or emergency device**. Do not rely on it as your only means of getting help. See [RESPONSIBLE_USE.md](RESPONSIBLE_USE.md).

## Repository layout

```
hardware/
  kicad/          KiCad project (schematic + PCB)
  libraries/      Custom symbols, footprints, 3D models
  production/     Gerbers, BOM, pick-and-place (published as Releases)
  enclosure/      Enclosure CAD (future)
firmware/         Device firmware
docs/             Requirements, architecture, bring-up guides
```

## License

| Part | License |
|---|---|
| Hardware (`hardware/`) | [CERN-OHL-S-2.0](LICENSE-HARDWARE) |
| Firmware (`firmware/`) | [GPL-3.0](LICENSE-FIRMWARE) |
| Documentation (`docs/`, README files) | [CC-BY-SA-4.0](LICENSE-DOCS) |

The **"Padma" name and logo are not covered by these licenses**. See [TRADEMARK.md](TRADEMARK.md).

Copyright © 2026 Sai Sandeep Lolla
