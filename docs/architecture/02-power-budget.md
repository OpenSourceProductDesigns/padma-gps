# 02 · Power Budget

Status: `draft`. All currents are **estimates from typical datasheet ranges for the part classes** in [01-system-block-diagram.md](01-system-block-diagram.md). Replace them with datasheet values once parts are shortlisted, and with measurements once there is an evaluation board.

## Battery assumptions

| Item | Value | Notes |
|---|---|---|
| Cell | Li-Po, **~300 mAh**, 3.7 V nominal | About 35 × 25 × 4 mm (a "402535" size). Uses most of the 46 × 39 mm footprint, leaving ~7 mm of the 11 mm height for PCB, parts and walls (NFR-001) |
| Usable fraction | **85 %** → **255 mAh** | Ageing, 0–50 °C operation, modem brown-out cutoff around 3.3–3.5 V |
| SOS reserve (FR-040) | **100 mAh** | One 30-minute SOS at the typical SOS current (below), plus ~10 % margin |
| Available for standby | **155 mAh** | 255 − 100 |

## SOS (active call) current

| Load | Low | Typ | High | Notes |
|---|---|---|---|---|
| Modem, VoLTE call | 100 | 150 | 250 | mA. Depends heavily on signal strength; the body-worn antenna pushes toward "high" (R-05) |
| GNSS tracking (L1 + L5) | 10 | 20 | 30 | mA. Could duty-cycle to one fix per T_track |
| MCU, audio streaming + PCM | 5 | 10 | 20 | mA |
| Mic (active mode), haptic, misc | 1 | 1 | 2 | mA |
| **Total** | **116** | **181** | **302** | mA |

- **30-minute reserve:** 58 / 90 / 151 mAh. The 100 mAh reserve covers the typical case, **not** the high case. If field tests show poor signal, increase the reserve or shorten the guaranteed call.
- **Longest SOS from a full battery** (255 mAh): 2.2 h / **1.4 h** / 0.8 h.

> ⚠ **NFR-011 (≥ 2 h of continuous SOS tracking) is met only in the best case.** Options: a larger cell (if the enclosure allows), duty-cycling GNSS hard after the first fix, switching to SMS-only location updates after a set call length, or lowering the target to ~1 h for v1. Needs a decision.

## Standby (armed) current

### Everything except the modem

| Load | Low | Typ | High | Notes |
|---|---|---|---|---|
| Mic, low-power mode + sound detect | 0.02 | 0.15 | 0.25 | mA. Stage 0 of the wake chain |
| MCU detection (stage 1 always on, stage 2 rare) | 0.20 | 0.50 | 1.20 | mA. **Biggest uncertainty**; depends on how often stage 1 wakes in a noisy city |
| IMU, motion wake | 0.005 | 0.02 | 0.05 | mA |
| GNSS breadcrumbs + backup domain | 0.04 | 0.16 | 1.00 | mA. Low: one 3 s fix every 30 min. Typ: 5 s every 15 min. High: 10 s every 5 min |
| PMIC, regulators, fuel gauge, flash sleep | 0.005 | 0.015 | 0.04 | mA |
| **Subtotal** | **0.27** | **0.85** | **2.54** | mA |

### Modem idle options (AD-05)

| Option | Low | Typ | High | What it costs |
|---|---|---|---|---|
| (a) Registered, LTE DRX ~1.28 s | 0.8 | 1.5 | 3.0 | mA. Always reachable; instant call setup |
| (b) PSM or eDRX | 0.01 | 0.1 | 0.5 | mA. Stays attached, so a call starts within a few seconds. **Depends on Jio / Airtel granting PSM / eDRX to a voice SIM**: unknown |
| (c) Off, booted on trigger | 0.005 | 0.01 | 0.02 | mA. Boot + attach + emergency call setup takes maybe 10–20 s: hidden by the 10 s countdown for automatic triggers, but at risk for manual SOS (NFR-020 ≤ 15 s). No OTA without waking |

### Standby life (155 mAh available)

| Option | Low load | **Typical** | High load |
|---|---|---|---|
| (a) Registered, DRX | 1.07 mA → 6.0 days | 2.35 mA → **2.7 days** | 5.54 mA → 1.2 days |
| (b) PSM / eDRX | 0.28 mA → 23 days | 0.95 mA → **6.8 days** | 3.04 mA → 2.1 days |
| (c) Off | 0.28 mA → 23 days | 0.86 mA → **7.5 days** | 2.56 mA → 2.5 days |

**Reading the table:**

- With the modem registered (a), the typical case is **~2.7 days**, which matches the "2–3 days realistic" note in NFR-010.
- **(b) gets close to the 7-day target**, and switching the modem fully off (c) adds very little over (b). If operators grant PSM / eDRX, (b) is the best option. If they don't, (c) is the fallback for automatic triggers, with a decision needed on manual SOS latency.
- Once the modem is handled, the **MCU detection current and the breadcrumb interval** dominate. Both are firmware-tunable.

### Breadcrumb interval sensitivity

Assuming a 5 s hot fix at 25 mA plus 0.02 mA backup:

| Interval | 5 min | 15 min | 30 min | 60 min |
|---|---|---|---|---|
| Average | 0.44 mA | 0.16 mA | 0.09 mA | 0.05 mA |

A 5-minute interval costs about as much as the whole detection chain. 15–30 minutes is the useful range, and it could adapt: more often when the IMU sees movement, less often when still.

## Peak current and supply

- An LTE module's Tx bursts can draw several hundred mA for a moment. A 300 mAh cell at 1C delivers only 300 mA continuously, so we need a **high-rate cell (≥ 2C)** and/or **bulk low-ESR capacitance on VBAT**. Check the voltage droop at low charge and at 0 °C against the modem's brown-out voltage.
- The haptic motor (~60–80 mA) can run at the same time as a Tx burst (the "call connected" pulse). Budget for it.

## Charging

- At ~1C (300 mA), a full charge takes about 1–1.5 h, which meets NFR-012 (≤ 2 h).

## What to measure first

1. Modem idle current in DRX, eDRX and PSM on **Jio and Airtel in Delhi**, and whether either network grants PSM / eDRX to a voice + SMS eSIM profile.
2. Modem time from off and from PSM to an answered 112 call (or a test number).
3. VoLTE call current at realistic body-worn signal levels.
4. MCU stage-1 wake rate and average current on a few hours of real street audio from Delhi.
