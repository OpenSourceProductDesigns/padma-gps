# 04 · Functional Requirements

Status: `draft`. Values marked **TBD** get fixed once size and battery trade-offs are known.

## Triggering & detection

| ID | Requirement | Pri | Trace |
|---|---|---|---|
| FR-001 | Device shall provide a **manual SOS trigger** that works even if automatic detection fails, using a gesture hard to activate by accident (physical button tentative; sealed touch / squeeze as alternatives; OQ-07). A manual SOS skips the countdown. | M | UC-01 |
| FR-002 | Device shall detect a **personal code phrase**, enrolled per wearer and accepted only in the **wearer's voice** (speaker verification), on-device and always on (OQ-15, R-08). | M | UC-04 |
| FR-003 | Device should detect **screams / distress sounds** on-device. | S | UC-04 |
| FR-004 | Audio for detection shall be processed **on-device only** and never stored or sent outside an active SOS call. | M | UC-04 |
| FR-005 | Detection models and thresholds shall be **updatable** through firmware. | S | UC-04 |
| FR-006 | Device shall have an **IMU** to detect **falls / struggle** and to confirm voice triggers (OQ-16). | M | UC-02, UC-03 |
| FR-007 | Device could log detection events (including cancelled ones) with the wearer's consent, to improve the models. | C | UC-04, UC-05 |

## Countdown & cancel (silent)

| ID | Requirement | Pri | Trace |
|---|---|---|---|
| FR-010 | The device shall produce **no audible output** at any point (no buzzer, siren or speaker). | M | UC-04, UC-08 |
| FR-011 | On automatic detection, the device shall wait a **cancel window** of T_cancel = **10 s** before calling (OQ-04). | M | UC-05 |
| FR-012 | The device shall tell the wearer discreetly, by **haptic only**, that a countdown is running (a distinct vibration pattern), and give one short pulse when the 112 call connects (OQ-12). | M | UC-05 |
| FR-013 | The wearer shall be able to **cancel** with a simple gesture. | M | UC-05 |
| FR-014 | Device could support a **duress cancel** (looks cancelled, still calls). | C | UC-06 |
| FR-015 | Status (armed, charging, low battery, no network) shall be visible only when the wearer checks it (e.g. LED on button press), never broadcast. | M | UC-12 |
| ~~FR-016~~ | ~~Loud siren mode~~: dropped; an audible device is easy for an attacker to find and discard. | W | |

## 112 voice call

| ID | Requirement | Pri | Trace |
|---|---|---|---|
| FR-020 | On SOS, the device shall **place a VoLTE voice call to 112**. | M | UC-08 |
| FR-021 | On answer, the device shall **play an automated announcement into the call** stating that it is a Padma GPS distress call, followed by the **location as lat/long and DIGIPIN**, spoken in **English** (OQ-13). | M | UC-07, UC-08 |
| FR-022 | After the announcement, the device shall stream the **MEMS microphone audio** into the call, with the downlink muted (nothing played on the device). | M | UC-08 |
| FR-023 | The device shall **repeat the location** every T_track during the call (in-call announcement and/or SMS to 112; OQ-02). | M | UC-07 |
| FR-024 | If the call fails or drops, the device shall **redial** with backoff until connected or the battery reserve runs out. | M | UC-08 |
| FR-025 | The device should also send an **SMS to 112** with location when SOS starts (no extra hardware; OQ-02). | S | UC-07 |
| FR-026 | An active SOS shall stop only when the **112 operator ends the call** or the wearer makes a **long press** on the device's input (OQ-11). Nothing else shall stop it. | M | UC-08 |
| ~~FR-027~~ | ~~SMS to trusted contacts~~: dropped for v1. | W | UC-11 |

## Location

| ID | Requirement | Pri | Trace |
|---|---|---|---|
| FR-030 | Device shall use **multi-constellation GNSS: GPS + NavIC** at minimum, plus Galileo, GLONASS and QZSS. The receiver shall support **BeiDou**, but official firmware keeps it **off by default** (OQ-08). | M | UC-07 |
| FR-031 | Device should support **dual-frequency L1 + L5** (NavIC is on L5; also better accuracy between tall buildings). | S | UC-07 |
| FR-032 | Device shall use **assisted GNSS / ephemeris caching** to speed up the first fix. | S | UC-07 |
| FR-033 | Device should fall back to **cell / Wi-Fi location** when there is no GNSS fix. | S | UC-10 |
| FR-034 | Device should keep a **low-rate breadcrumb** while idle so a last known fix is available immediately. | S | UC-07 |

## Power & platform

| ID | Requirement | Pri | Trace |
|---|---|---|---|
| FR-040 | Device shall **reserve battery** for at least one full SOS (TBD: e.g. 30 min call + location updates) and warn the wearer before reaching it. | M | UC-14 |
| FR-041 | Device shall charge via **USB-C or magnetic pogo pins** (whichever allows the smaller design). | M | UC-12 |
| FR-042 | The device shall be **reflashable by its owner** with custom firmware over a documented interface (USB bootloader and/or SWD pads); pinout, memory map and modem/GNSS control shall be documented. | M | UC-15 |
| FR-043 | Official firmware updates should be possible **over the air** (cellular) and over USB. | S | FR-005 |
| FR-044 | Device could detect removal / tamper. | C | UC-09 |
| FR-045 | Device shall have a **self-test** (network registration, GNSS, battery, mic). | S | UC-12 |
| FR-046 | The SIM shall be a soldered **eUICC (MFF2 or BGA eSIM)** supporting **GSMA Remote SIM Provisioning (RSP)**, so operator profiles can be downloaded, switched and deleted without physical access. Prefer the IoT variant (**SGP.32**), which suits a device with no screen; SGP.02 (M2M) is the fallback (OQ-09, A-02). | M | UC-12 |
