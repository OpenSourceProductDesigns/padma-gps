# 04 · GNSS Receiver Selection

Status: `draft`. The candidate list comes from vendor pages and news (2026-11-05). Each candidate still has to be **screened against its datasheet** (`hardware/datasheets/`, converted with `tools/pdf2md.py`).

## What the receiver must do

| # | Criterion | Source | Gate? |
|---|---|---|---|
| G1 | **NavIC** tracking (the satellites in service broadcast on **L5**) | FR-030 | **Yes** |
| G2 | GPS + Galileo + GLONASS + QZSS; **BeiDou supported but switchable off** by configuration | FR-030, OQ-08 | **Yes** |
| G3 | **Dual-frequency L1 + L5**, for NavIC and for accuracy between tall buildings | FR-031, AD-04 | Strong (implied by G1) |
| G4 | Size: small LGA, ideally ≤ ~12 × 16 mm | NFR-001 | Strong |
| G5 | Low power: tracking current, **hot-start** current and time, backup (RTC + ephemeris) current | NFR-010, power budget (breadcrumbs) | Strong |
| G6 | Assisted GNSS / ephemeris injection from the MCU (the modem can fetch it) | FR-032, NFR-022 | Strong |
| G7 | UART interface (+ 1PPS), documented binary protocol, reset / power control | AD-04 interface table | Strong |
| G8 | Works with a small body-worn antenna: integrated-antenna options, LNA / active-antenna support, jamming / interference tolerance near the LTE transmitter | R-05, AD-06 | Strong |
| G9 | Accuracy ≤ 10 m CEP50 in the open (dual-band parts claim ~1–2 m) | NFR-021 | Check |

## Candidates to screen

| Module | Notes from vendor pages (not yet screened) | First impression |
|---|---|---|
| ~~u-blox MAX-M10S~~ | M10 is **L1-only**: GPS / GLONASS / Galileo / BeiDou / QZSS / SBAS. **No NavIC** | Reject (fails G1) |
| **u-blox NEO-F10N** | F10 platform, L1 + L5. Signals: GPS L1C/A + L5, Galileo E1 + E5a, BeiDou B1 + B2a, QZSS, **NavIC L5**. ~12.2 × 16 mm | Screen |
| **u-blox DAN-F10N** | Same F10 engine with an **integrated L1 / L5 antenna**, marketed as the smallest dual-band module with an antenna (Mar 2025). Could ease R-05 | Screen; size and antenna performance are key |
| **Quectel LC79H (AL)** | **Screened (brochure V8.6):** AG3335M · GPS / QZSS L1 C/A + L5, GLONASS L1, Galileo E1 + E5a, BDS B1I + B2a, **NavIC L5** · LCC **10.1 × 9.7 × 2.4 mm**, 0.5 g · **VCC 1.75–1.98 V** (fits our 1.8 V rail) · 33 mA tracking, **20 µA backup** · hot start 1 s, cold 26 s · 1.0 m CEP · built-in LNA, jamming detection **and anti-jamming** · UART / I²C, 1PPS, RESET · A-GNSS | **Lead candidate.** Check: the brochure lists I/O as 2.8 V, which contradicts the 1.8 V supply (needs the datasheet); tracking current is high (duty-cycle the breadcrumbs) |
| Quectel LC29H (AA) | **Screened (brochure V8.6):** AG3335M · same L1 + L5 signal set, **NavIC L5** · 12.2 × 16.0 × 2.5 mm · VCC 3.1–3.6 V · 24 mA tracking, 25 µA backup · 1.0 m CEP · jamming detection, **no anti-jamming** | Backup option. Bigger and needs a 3.3 V rail |
| Quectel LC29H (AI) | Brochure lists GPS / GLONASS / Galileo / BDS / QZSS / **NavIC** / SBAS, 16 mA, 51 µA backup, 1.8 m CEP. Signal bands not shown | Check whether it is L1 + L5 |
| Quectel L89 R2.0 | AG3335, has NavIC L5, but **26.4 × 18.4 × 6.8 mm** | Reject (fails G4) |

## Open checks

- Does the LTE transmitter (B5 / B8 harmonics, B40 / B41 near L1) desensitize the receiver in a small enclosure? Ask for the jamming and blocking specs; it will need a SAW filter or LNA choice (G8).
- NavIC on **L1** (the new NVS series satellites) would let an L1-only receiver use NavIC in future. Today too few satellites broadcast it, so L5 stays a gate.

## Sources

- Quectel Product Brochure V8.6, GNSS section (local copy in `hardware/datasheets/Quectel/`)
- u-blox MAX-M10S datasheet: <https://content.u-blox.com/sites/default/files/MAX-M10S_DataSheet_UBX-20035208.pdf>
- u-blox NEO-F10N datasheet: <https://content.u-blox.com/sites/default/files/documents/NEO-F10N_DataSheet_UBX-23002117.pdf>
- DAN-F10N news: <https://www.cnx-software.com/2025/03/20/u-blox-dan-f10n-the-worlds-smallest-dual-band-l1-l5-gnss-module-with-an-integrated-antenna/>
- Quectel LC79H: <https://www.quectel.com/blog/document/gnss-lc79h-series/>
- Quectel LC29H spec V1.2: <https://quectel.com/content/uploads/sites/3/2022/06/Quectel_LC29H_GNSS_Specification_V1.2.pdf>
- Quectel L89 R2.0: <https://www.4gltemall.com/quectel-l89-r2-0.html>
