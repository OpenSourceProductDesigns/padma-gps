# 05 · Non-Functional Requirements

Status: `draft`

## Size & wearability

| ID | Requirement | Pri |
|---|---|---|
| NFR-001 | Enclosure shall fit within a **smartwatch-sized envelope**: ≤ ~46 × 39 × 11 mm (reference: 45 mm Apple Watch case ≈ 45 × 38 × 10.7 mm). Smaller is better. | M |
| NFR-002 | Form factor: **pendant** worn around the neck (primary); **adhesive / clip patch** (alternative). | M |
| NFR-003 | Mass: TBD (target ≤ 30 g). | S |
| NFR-004 | Look: discreet; should not obviously read as a safety device (it could pass as jewellery or a tag). | S |

## Battery

| ID | Requirement | Pri |
|---|---|---|
| NFR-010 | Standby with idle breadcrumbs: **≥ 1 day minimum, target ≥ 7 days**. | M / S |
| NFR-011 | Continuous SOS tracking: TBD (target ≥ 2 h at T_track). | M |
| NFR-012 | Full charge ≤ 2 h. | S |

> Rough feasibility note: a watch-sized enclosure fits about 200–350 mAh. A VoLTE call on LTE Cat 1 bis draws roughly 100–250 mA (a 30 min call ≈ 50–125 mAh, which sets the reserve). **Always-on audio detection is now the main standby load**: a low-power MEMS microphone with voice-activity wake plus an MCU running keyword spotting can average roughly 0.3–1.5 mA, which alone is ~1–2 weeks on 300 mAh before the modem is counted. The modem must stay registered for 112, ideally in eDRX or a low-power idle mode, and GNSS stays off except for breadcrumbs. **Seven days is ambitious; 2–3 days is realistic for v1.** We will model this in the architecture phase.

## Performance

| ID | Requirement | Pri |
|---|---|---|
| NFR-020 | Trigger to 112 call initiated: ≤ 25 s for automatic triggers (T_cancel 10 s + 15 s); ≤ 15 s for manual SOS. | M |
| NFR-021 | Location accuracy outdoors: ≤ 10 m (CEP50) in the open, ≤ 25 m in urban canyons. | S |
| NFR-022 | Warm-start TTFF ≤ 5 s; cold start with assistance ≤ 30 s. | S |
| NFR-023 | **False positive rate** of automatic detection reaching 112 (after the cancel window): TBD (target < 1 per wearer per year). | M |
| NFR-024 | **False negative rate:** TBD, measured against a defined test set of falls and struggles. | M |

## Robustness

| ID | Requirement | Pri |
|---|---|---|
| NFR-030 | Water / dust: **IP67** target (sweat, rain, washing hands). | S |
| NFR-031 | Survives drops from 1.5 m onto concrete, and a strong pull on the lanyard. | S |
| NFR-032 | Operating temperature: 0–50 °C ambient (Delhi summers: the enclosure sits in the sun against the body). | M |

## Privacy & security

| ID | Requirement | Pri |
|---|---|---|
| NFR-040 | **No continuous location or audio upload** outside SOS, unless the wearer explicitly opts in. | M |
| NFR-041 | Audio for detection is processed **on-device only**. | M |
| NFR-042 | Comply with India's **DPDP Act 2023** for any personal data handled. | M |
| NFR-043 | Official firmware updates shall be **signed**. Secure boot / debug lock, if used, shall be **owner-controlled** (the owner can enrol their own key or unlock it), so it never blocks reflashing (FR-042). | S |
| NFR-044 | Official firmware shall have **no covert-tracking mode**: it only calls 112 on SOS, with no remote location polling by third parties. | M |

## Regulatory (India)

| ID | Requirement | Pri |
|---|---|---|
| NFR-050 | Cellular module / device: **TEC MTCTE** certification; operator acceptance (VoLTE on Jio / Airtel). | M |
| NFR-051 | Radio: **WPC** equipment type approval (ETA). | M |
| NFR-052 | Battery and charger: **BIS** (CRS) where applicable. | M |
| NFR-053 | Explore relevant panic-button / IRNSS standards (e.g. how AIS-140 handles panic alerts and NavIC) as a precedent for ERSS integration. | S |

## Cost

| ID | Requirement | Pri |
|---|---|---|
| NFR-060 | Target retail ≤ ₹10,000 for v1. Cost is secondary to reliability. | C |
