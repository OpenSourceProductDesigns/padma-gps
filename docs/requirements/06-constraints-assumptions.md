# 06 · Constraints, Assumptions, Open Questions & Risks

Status: `draft`

## Constraints

- C-01: **Standalone**, so no smartphone is required for any core function.
- C-02: Initial market **India**, starting with **Delhi NCR**, then Hyderabad.
- C-03: Size no larger than a smartwatch case (NFR-001).
- C-04: Open hardware / firmware licences (CERN-OHL-S, GPL-3.0).
- C-05: **Silent device**: no audible output (FR-010).
- C-06: **Core hardware:** LTE Cat 1 bis modem with VoLTE, multi-constellation GNSS (with NavIC), MEMS microphone, ARM MCU for detection. Plus: battery + charger, SIM / eSIM, LTE and GNSS antennas, a button; optional haptic motor and IMU.

## Assumptions

- A-01: India's 2G/3G networks are being phased out; **LTE with VoLTE** is the safe long-term bearer. Cat 1 bis is the leading candidate.
- A-02: The wearer keeps an active SIM / eSIM plan with voice and SMS.
- A-03: 112 is reachable by voice call (and SMS) from any Indian mobile connection.
- A-04: The cellular module can **inject pre-recorded audio / TTS into the uplink** of an active call and mute the downlink (true of many modules; verify on the shortlisted parts).

## Open questions

| ID | Question | Status |
|---|---|---|
| OQ-01 | How does a standalone device deliver location to ERSS? | **Partly answered:** the channel is a VoLTE call with a spoken announcement + location. Still open: does ERSS also get network location for the caller's number, and is there a data path? |
| OQ-02 | How are location updates delivered during the call: repeated in-call announcement, SMS to 112, or both? Does ERSS parse SMS location? | Open (FR-023, FR-025) |
| ~~OQ-03~~ | ~~Trusted-contact SMS in v1?~~ | **Answered: no** (Won't for v1) |
| OQ-04 | T_cancel length: 10 s vs 30 s? | Open |
| OQ-05 | Countdown feedback: buzzer, speaker or vibration? | **Answered:** nothing audible. Haptic is still open, see OQ-12 |
| OQ-06 | Speaker + mic for a two-way call? | **Answered:** mic only, listen-in; no speaker |
| OQ-07 | Should manual SOS skip the countdown? | Open. Suggest: no countdown for manual SOS |
| OQ-08 | Include BeiDou? | Leaning **yes** ("use all constellations"); check for any procurement or perception issue in India |
| OQ-09 | SIM: nano-SIM vs **eSIM / MFF2** (smaller, sealed, better for IP67)? | Open. Suggest MFF2 / eSIM |
| OQ-10 | Which ARM MCU for on-device speech recognition? | **Partly answered:** ARM Cortex-M class. Candidates: Cortex-M4F / M33 (classic keyword spotting), Cortex-M55 + Ethos-U NPU (e.g. Alif Ensemble) for scream + keyword detection at lower power, or the modem's own application core (OpenCPU) to save a chip. |
| OQ-11 | Who can stop an active SOS? An attacker must not be able to | Open. Suggest: only the 112 operator hanging up, or a long secret gesture |
| OQ-12 | **Haptic** countdown (a coin vibration motor, ~8 mm)? Without it the wearer cannot know a false trigger is in progress and cancel it | **New.** Strongly suggested: false calls to 112 are the main product risk |
| OQ-13 | Announcement content: plain lat/long digits, a shorter code (e.g. Plus Code / DIGIPIN), nearest landmark? Language (Hindi / English)? | **New** |
| OQ-14 | How do 112 operators handle **silent calls**? Many centres hang up on silence; the announcement must come immediately and maybe repeat | **New.** Ask ERSS / Delhi Police |
| OQ-15 | Which keyword(s)? Common words ("help", "bachao") cause more false triggers than a personal code phrase; per-user enrolment? | **New** |
| OQ-16 | Keep an IMU for fall / struggle detection? It is tiny (~2 × 2 mm) and low power, and can also confirm voice triggers (scream + sudden motion = higher confidence) | **New.** Suggest keeping it |

## Risks

| ID | Risk | Impact | Mitigation |
|---|---|---|---|
| R-01 | ERSS treats an automated or silent call as a nuisance and hangs up | High | Clear announcement at once (OQ-14); engage ERSS / Delhi Police early |
| R-02 | False triggers lead to unwanted 112 calls | High: trust, legal | Cancel window + haptic (OQ-12), conservative thresholds, multi-signal confirmation (voice + IMU) |
| R-03 | Battery too small for always-on audio + an LTE reserve | Medium | Microphone with hardware voice-activity wake, NPU MCU; accept 2–3 days in v1 |
| R-04 | GNSS poor indoors / in the metro | Medium | Breadcrumbs, cell / Wi-Fi fallback |
| R-05 | LTE + GNSS antenna performance in a watch-sized, body-worn enclosure | **High** | Early antenna study; consider a lanyard / ring antenna on the pendant |
| R-06 | Certification cost and time (MTCTE, WPC, BIS) | Medium | Pre-certified modem module |
| R-07 | **Misuse:** the reflashable LTE + GNSS + mic platform repurposed for stalking or covert listening | High: reputational | Accepted as an unavoidable side effect of an open platform. Open licences **cannot restrict field of use** (CERN-OHL-S / GPL govern copying and modification, not purpose). Levers we do have: **trademark** (modified or misused builds can't be called "Padma"), RESPONSIBLE_USE.md, and no covert features in official firmware (NFR-044). |
