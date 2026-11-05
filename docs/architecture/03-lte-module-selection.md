# 03 · LTE Module Selection

Status: `draft`. Data comes from vendor **product specifications** (short datasheets) read on 2026-11-05. Full hardware design guides, AT manuals and certificates still need to be checked; see [Open checks](#open-checks).

## What the module must do

Taken from the requirements and [01-system-block-diagram.md](01-system-block-diagram.md):

| # | Criterion | Source | Gate? |
|---|---|---|---|
| K1 | LTE bands for Jio / Airtel / Vi: **B1, B3, B5, B8 (FDD) + B40, B41 (TDD)** | NFR-050 | **Yes** |
| K2 | **VoLTE**, including **IMS emergency calls to 112** (Jio is VoLTE-only, and 2G/3G are being switched off) | FR-020, A-01 | **Yes** |
| K3 | **Digital audio (PCM / I²S) usable in a VoLTE call**, so the MCU can inject the announcement and mic audio; downlink can be muted | AD-01, A-04 | **Yes** (an analog mic input is a fallback, see below) |
| K4 | Size: as small as possible. The footprint has to share 46 × 39 mm with the battery and the other parts | NFR-001 | Strong |
| K5 | Low idle current in DRX, plus PSM / eDRX support | NFR-010, AD-05 | Strong |
| K6 | eSIM / eUICC support, ideally **SGP.32** remote provisioning | FR-046 | Strong |
| K7 | India certification: TEC MTCTE, plus a track record on Jio / Airtel | NFR-050, R-06 | Strong |
| K8 | Cat 1 bis, single antenna (no diversity antenna to fit) | AD-06 | Strong |

Built-in GNSS is **not** a criterion: AD-04 uses a separate L1 + L5 receiver for NavIC.

## Candidates compared

✅ = stated in the vendor spec · ⚠ = optional / "in development" / unclear · ❌ = not supported · ? = not stated

| Module | Chipset | Cat | K1 India bands | K2 VoLTE | K3 Digital audio | K4 Size (mm) | K5 Sleep current | K6 eSIM | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Quectel EG915U-CN** | UNISOC 8910DM (to confirm) | 1 bis | ✅ FDD B1/3/5/8 · TDD B34/38/39/40/41 · "China / India" variant | ✅ | ✅ PCM ×1 · analog mic too | 23.6 × 19.9 × 2.4 LGA | 1.2 mA @ PF = 256 · 13 mA idle · 32 µA off | ✅ (eSIM row in spec) | **Lead candidate** |
| SIMCom SIM7672S | Qualcomm QCX216 | 1 bis | ✅ FDD B1/3/5/8 · TDD B34/38/39/40/41 | ❌ **"NA" for all variants** | ✅ PCM | 24 × 24 × 2.4 LCC+LGA | **0.8 mA @ DRX 0.64 s** · 4.2 mA idle · PSM 3 µA | ⚠ SGP.32 firmware being added | Reject: no VoLTE. Re-check if SIMCom adds it (best sleep current) |
| Quectel EG800Q-IN | ? | 1 bis | ✅ FDD B1/3/5/8 · TDD B40/41 | ? not listed | ⚠ PCM "in development" | **17.7 × 15.8 × 2.4** LGA (smallest) | 3.9 mA idle · 45 µA CFUN=0 · 1.5 µA off | ? (eSIM note only for EU variant) | **Watch**: best size and power, but no voice today |
| SIMCom A7672S | ASR1603 | 1 | ✅ FDD B1/3/5/8 · TDD B34/38/39/40/41 + GSM | ⚠ reseller claims only | ❌ analog mic / speaker only | 24 × 24 × 2.4 | "TBD" | ⚠ SGP.32 firmware being added | Reject: no digital audio, older platform |
| Quectel EC200U-CN | UNISOC 8910DM | 1 | ✅ FDD B1/3/5/8 · TDD B34/38/39/40/41 | ? | ⚠ analog; PCM not shown | **31 × 28 × 2.4** | 1.2 mA @ PF = 256 | ? | Reject: too big (same silicon as EG915U) |
| Cavli C16QS-IN-GNAH | QCX216 class | 1 bis | ✅ B1/3/5/8/40/41 | ? | ⚠ I²S ×1 "requires SDK" | 26.5 × 22.5 × 2.3 | 11 µA hibernate | ✅ integrated eSIM | Reject for now: big, VoLTE not stated. Indian vendor, so keep in view |
| Telit ELS63-I / -IG | ? | 1 bis | ✅ B1/3/5/8/40/41 (-IG adds NavIC GNSS) | ? (data-only positioning) | ? not listed | 27.6 × 18.8 × 2.4 | ? | ❌ external SIM | Reject: data-only |
| Telit LE910R1-EA | ? | 1 bis | ⚠ has B1/3/5/8/40/41, but no India variant | ✅ | ? | 28.2 × 28.2 × 2.2 | ? | ? | Reject: size, no India variant |

## Recommendation

1. **Lead: Quectel EG915U-CN.** It is the only part whose own spec sheet confirms all three gates: India bands (the variant is labelled "China / India"), **VoLTE**, and a **PCM** digital audio port. It also has an analog mic input as a fallback, and an eSIM row. Its weaknesses are size (23.6 × 19.9 mm, about 25 % of the 46 × 39 mm footprint) and a higher idle current than the Qualcomm part. 1.2 mA at PF = 256 still fits the power budget's option (a) estimate (0.8–3.0 mA).
2. **No runner-up yet.** The SIM7672S looked strong on power (0.8 mA sleep, 3 µA PSM), but its spec sheet lists **VoLTE as "NA" for every variant**. Re-check it if SIMCom adds VoLTE in a later firmware. Finding a second VoLTE-capable part is an open task (see "Not yet evaluated" below).
3. **Watch: Quectel EG800Q-IN.** 30 % smaller than the EG915U and lower power, but voice and PCM are not released yet. If Quectel ships VoLTE + PCM on the IN variant, it becomes the best fit. The family is pin-compatible across regions, so it could be a v2 drop-in.

**Next step:** buy an EVB for the **EG915U-CN** and run the A-04 test from the block diagram first: a VoLTE call on Jio and Airtel in Delhi with PCM audio injected into the uplink and the downlink muted. Use a test number first, then a coordinated 112 test call.

### Fallback if PCM fails in VoLTE calls

AD-01 assumes digital audio. If a module only passes audio properly through its **analog mic input** during VoLTE, the MCU can drive that input from a DAC or filtered PWM output. This costs an op-amp and some board area, and adds a little noise, but it keeps "one MEMS mic routed through the MCU". Keep it as plan B. It is not a reason to pick an analog-only module.

## Open checks

Ask the vendors these before ordering EVBs:

| # | Question | EG915U-CN | SIM7672S | EG800Q-IN |
|---|---|---|---|---|
| Q1 | **IMS emergency call (112) over VoLTE** works, with and without a SIM, on Jio and Airtel | ask | no VoLTE | ask |
| Q2 | PCM audio active during a **VoLTE** call (not only CS voice). Can the downlink be muted (`AT+CMUT`-type commands)? Supported sample rates (8 / 16 kHz)? | ask | no VoLTE | ask |
| Q3 | VoLTE profile tested on Jio / Airtel / Vi (IMS config, carrier IOT) | ask | will VoLTE be added? | ask |
| Q4 | **TEC MTCTE** certificate for this exact variant | ask | ask | ask |
| Q5 | eSIM: does it support an external MFF2 eUICC? Is an SGP.32 IPA (IoT Profile Assistant) in the module firmware? | ask | ask | ask |
| Q6 | PSM / eDRX current, and whether Indian operators grant PSM / eDRX to voice SIMs (AD-05) | ask | ask | ask |
| Q7 | Peak current during a Tx burst (sizes the VBAT bulk capacitance and the battery C-rate) | ask | ask | ask |
| Q8 | Chipset confirmation (EG915U is believed to be UNISOC 8910DM) | ask | – | ask |

Not yet evaluated: Quectel **EG810M** (also listed for China / India), Fibocom and MeiG Cat 1 bis parts, and u-blox **LENA-R8**.

## Sources

- Quectel EG915U Series spec V1.8: <https://www.quectel.com/blog/document/lte-cat-1-bis-eg915u-series>
- Quectel EG800Q Series spec V1.9: <https://www.quectel.com.cn/wp-content/uploads/2026/01/Quectel_EG800Q系列_LTE_Standard_模块产品规格书_V1.9.pdf>, product page <https://www.quectel.com/product/lte-eg800q-series/>
- Quectel EC200U Series spec V1.4: <https://python.quectel.com/en/wp-content/uploads/sites/2/2024/11/Quectel_EC200U_Series_LTE_Standard_Specification_V1.4.pdf>
- SIMCom SIM7672 Series spec (2023-12): <https://edworks.co.kr/wp-content/uploads/2024/07/SIM7672-Series_Spec_231205.pdf>, product page <https://en.simcom.com/product/SIM7672.html>
- SIMCom A7672S spec (2020-12): <https://www.rhydolabz.com/documents/30/A7672S_Specifications.pdf>; A7672X / A7670X Hardware Design V1.03: <https://files.waveshare.com/wiki/A7670E-Cat-1-GNSS-HAT/A7672X_A7670X_Series_Hardware_Design_V1.03.pdf>
- SIMCom SGP.32 announcement: <https://en.simcom.com/news_view-445.html>
- Cavli C16QS: <https://www.cavliwireless.com/c-series/c16qs.html>, spec V2.7 <https://shop.mev-elektronik.com/wp-content/uploads/C16QS-Cat1.bis-Technical-Specification-Document-V2.7.pdf>
- Telit ELS63: <https://www.telit.com/devices/els63/> · LE910R1: <https://www.telit.com/devices/le910r1-series/>
