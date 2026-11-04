# 06 · Constraints, Assumptions, Open Questions & Risks

Status: `draft`

## Constraints

- C-01: **Standalone**, so no smartphone is required for any core function.
- C-02: Initial market **India**, starting with **Delhi NCR**, then Hyderabad.
- C-03: Size no larger than a smartwatch case (NFR-001).
- C-04: Open hardware / firmware licences (CERN-OHL-S, GPL-3.0).
- C-05: **Silent device**: no audible output (FR-010).
- C-06: **Core hardware:** LTE Cat 1 bis modem with VoLTE, multi-constellation GNSS (with NavIC), MEMS microphone, ARM MCU for detection, IMU, haptic motor. Plus: battery + charger, soldered **eSIM (MFF2 or BGA) with remote SIM provisioning** (FR-046), LTE and GNSS antennas; a physical button is tentative (OQ-07).

## Assumptions

- A-01: India's 2G/3G networks are being phased out; **LTE with VoLTE** is the safe long-term bearer. Cat 1 bis is the leading candidate.
- A-02: The wearer keeps an active eSIM plan with voice and SMS. **To verify:** Indian operators (Jio, Airtel, Vi) offer eSIM profiles with **VoLTE and SMS** (not data-only IoT plans), downloadable via remote SIM provisioning to an IoT device.
- A-03: 112 is reachable by voice call (and SMS) from any Indian mobile connection.
- A-04: The cellular module can **inject pre-recorded audio / TTS into the uplink** of an active call and mute the downlink (true of many modules; verify on the shortlisted parts).

## Open questions

| ID | Question | Status |
|---|---|---|
| OQ-01 | How does a standalone device deliver location to ERSS? | **Partly answered:** the channel is a VoLTE call with a spoken announcement + location. Still open: does ERSS also get network location for the caller's number, and is there a data path? |
| OQ-02 | How are location updates delivered during the call: repeated in-call announcement, SMS to 112, or both? Does ERSS parse SMS location? | Open (FR-023, FR-025) |
| ~~OQ-03~~ | ~~Trusted-contact SMS in v1?~~ | **Answered: no** (Won't for v1) |
| ~~OQ-04~~ | ~~T_cancel length: 10 s vs 30 s?~~ | **Answered: 10 s.** If a false trigger still gets through, the wearer can explain to the operator over the open mic, or the operator ends the call (FR-011) |
| ~~OQ-05~~ | ~~Countdown feedback: buzzer, speaker or vibration?~~ | **Answered:** nothing audible; haptic only (OQ-12) |
| ~~OQ-06~~ | ~~Speaker + mic for a two-way call?~~ | **Answered:** mic only, listen-in; no speaker |
| OQ-07 | Physical button for manual SOS? | **Tentatively kept.** Trade-off: space, enclosure design and IP67 sealing vs. a trigger that works when voice fails (R-08). Alternatives: sealed capacitive touch area, or squeeze detected by the IMU. If kept, manual SOS skips the countdown |
| ~~OQ-08~~ | ~~Include BeiDou?~~ | **Answered:** the receiver shall support it, but it is **off by default** in official firmware (perception / NavIC policy). Revisit if field tests show slow or poor fixes (FR-030) |
| ~~OQ-09~~ | ~~SIM: nano-SIM vs eSIM / MFF2?~~ | **Answered:** soldered **eSIM, MFF2 or BGA package**, with remote SIM provisioning (FR-046). Check A-02 |
| OQ-10 | Which ARM MCU for on-device speech recognition? | **Partly answered:** ARM Cortex-M class. Candidates: Cortex-M4F / M33 (classic keyword spotting), Cortex-M55 + Ethos-U NPU (e.g. Alif Ensemble) for scream + keyword detection at lower power, or the modem's own application core (OpenCPU) to save a chip. **Speaker verification (OQ-15) is much heavier than keyword spotting and favours the M55 + NPU class.** |
| ~~OQ-11~~ | ~~Who can stop an active SOS?~~ | **Answered:** only the **112 operator** (ending the call) or a **long press** on the device's input (button, or sealed touch / squeeze if the button is dropped) (FR-026) |
| ~~OQ-12~~ | ~~Haptic countdown?~~ | **Answered: yes.** Coin vibration motor (~8 mm): a discreet pattern during the countdown, and one short pulse when the 112 call connects (FR-012) |
| ~~OQ-13~~ | ~~Announcement content and language?~~ | **Answered:** **lat/long + DIGIPIN**, in **English**. English works for 112 operators across India, including the south; Hindi alone would not (FR-021). Verify with ERSS that DIGIPIN is usable |
| OQ-14 | How do 112 operators handle **silent calls**? Many centres hang up on silence; the announcement must come immediately and maybe repeat | Open. Ask ERSS / Delhi Police |
| ~~OQ-15~~ | ~~Which keyword(s)?~~ | **Answered:** a **personal code phrase**, enrolled per wearer and accepted only in the **wearer's voice** (speaker verification, like "Hey Google" voice match). Revisit if the chosen hardware cannot do it within the power budget (FR-002, R-08) |
| ~~OQ-16~~ | ~~Keep an IMU?~~ | **Answered: yes.** Fall / struggle detection, and confirmation of voice triggers (FR-006) |

## Risks

| ID | Risk | Impact | Mitigation |
|---|---|---|---|
| R-01 | ERSS treats an automated or silent call as a nuisance and hangs up | High | Clear announcement at once (OQ-14); engage ERSS / Delhi Police early |
| R-02 | False triggers lead to unwanted 112 calls | High: trust, legal | 10 s cancel window + haptic (FR-011, FR-012), personal code phrase + voice match (FR-002), conservative thresholds, multi-signal confirmation (voice + IMU) |
| R-03 | Battery too small for always-on audio + an LTE reserve | Medium | Microphone with hardware voice-activity wake, NPU MCU; accept 2–3 days in v1 |
| R-04 | GNSS poor indoors / in the metro | Medium | Breadcrumbs, cell / Wi-Fi fallback |
| R-05 | LTE + GNSS antenna performance in a watch-sized, body-worn enclosure | **High** | Early antenna study; consider a lanyard / ring antenna on the pendant |
| R-06 | Certification cost and time (MTCTE, WPC, BIS) | Medium | Pre-certified modem module |
| R-07 | **Misuse:** the reflashable LTE + GNSS + mic platform repurposed for stalking or covert listening | High: reputational | Accepted as an unavoidable side effect of an open platform. Open licences **cannot restrict field of use** (CERN-OHL-S / GPL govern copying and modification, not purpose). Levers we do have: **trademark** (modified or misused builds can't be called "Padma"), RESPONSIBLE_USE.md, and no covert features in official firmware (NFR-044). |
| R-08 | **Voice mismatch under stress:** a screaming, whispering or crying wearer does not match their enrolled voice, so a real emergency is rejected | **High** | Looser speaker-verification threshold, with false triggers caught by the cancel window; scream detection and IMU as extra triggers; a manual trigger (button, touch or squeeze; OQ-07) that does not depend on voice; test enrolment against stressed speech |
