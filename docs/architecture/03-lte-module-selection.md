# 03 · LTE Module Selection

Status: `draft`. **Vendor search concluded 2026-11-05**; the shortlist now waits on vendor answers and EVB tests. Data comes from vendor **product specifications, product briefs and data sheets** read on 2026-11-05. Full hardware design guides, AT manuals and certificates still need to be checked; see [Open checks](#open-checks).

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

Built-in GNSS is **not** a criterion: AD-04 uses a separate L1 + L5 receiver for NavIC (see [04-gnss-selection.md](04-gnss-selection.md)).

## Vendor policy

Decided 2026-11-05: **use non-Chinese module vendors. Quectel is the one exception**, kept for its maturity, documentation and India track record. Other Chinese vendors (SIMCom, Fibocom, MeiG, Neoway, Lierda, …) are out of scope and are not screened.

## Shortlist

| Rank | Module | Why | Main open question |
|---|---|---|---|
| 1 | **Quectel EG915U-CN** | Only part whose own spec confirms all three gates: India variant, VoLTE, PCM | Which order code has voice enabled (Q9) |
| 2 | **Telit ELS62-I** | Second source from a non-Chinese vendor: India variant, VoLTE, PCM / I²S on paper | Size and sleep current (not in the brief); India approval |

## Candidates compared

**Scope:** only parts with a vendor datasheet, spec or brief in `hardware/datasheets/` are compared. These were handpicked by the user as Cat 1 bis parts that might have VoLTE. Parts seen only in the Quectel brochure or on web pages (EG810M, EG800Q / K / AK, EC800UG, EG915N / Q, Telit LE310Q1 / X1, LE910Q1, SIMCom) are out of scope. Most of them lack VoLTE anyway.

✅ = stated in the vendor document · ⚠ = optional / "in development" / unclear · ❌ = not supported · ? = not stated

| Module | Chipset | Cat | K1 India bands | K2 VoLTE | K3 Digital audio | K4 Size (mm) | K5 Sleep current | K6 eSIM | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Quectel EG915U-CN** | UNISOC 8910DM (to confirm) | 1 bis | ✅ FDD B1/3/5/8 · TDD B34/38/39/40/41 · "China / India" variant | ✅ spec V1.8 lists VoLTE for all three variants, but under a **"Voice (Optional)"** section (brochure V8.6 also says "Optional"), so order the voice build | ✅ PCM ×1 · analog mic too | 23.6 × 19.9 × 2.4 LGA | 1.2 mA @ PF = 256 · 13 mA idle · 32 µA off | ✅ (eSIM row in spec) | **Lead candidate** |
| **Telit ELS62-I** | ? | 1 bis (Rel 13) + EGPRS | ✅ **India variant**: FDD B1/3/5/8 · TDD B40/41 · GSM 900/1800 | ✅ "VoLTE with CSFB" (brief) | ✅ **PCM and I²S** | ? not in brief ("Industrial" form factor; confirm) | ? | ⚠ "embedded SIM option" | **Second source.** Passes K1–K3 on paper. Need the datasheet for size and sleep current. No India approval listed (GCF, RED, … only) |
| Quectel EC200U-CN | UNISOC 8910DM | 1 | ✅ FDD B1/3/5/8 · TDD B34/38/39/40/41 | ? | ✅ PCM ×1 + analog (spec V1.8) | **31 × 28 × 2.4** | 1.2 mA @ PF = 256 | ? | Reject: too big (same silicon as EG915U) |
| Quectel EG912U-GL / -EAL | ? | 1 bis | ⚠ no India variant; TDD B34/38/39/40/41 on GL | ✅ spec V1.6 | ✅ PCM ×1 + analog | **29.0 × 25.0 × 2.4** | 1.2 mA @ PF = 256 | ? | Reject: too big, no India variant |
| Telit ELS63-I / -IG | ? | 1 bis (Rel 14) | ✅ B1/3/5/8/40/41 (-IG adds GNSS **with NavIC**) | ❌ brief: "aims at data-only IoT applications" | ❌ not listed | 27.6 × 18.8 × 2.4 | ? | ❌ external SIM | Reject: data-only (confirmed in brief) |
| Telit LE910R1-EA | ? | 1 bis (Rel 13) + 2G | ✅ EA has B1/3/5/8/40/41 (EMEA / APAC variant, not India-specific) | ✅ "VoLTE support" | ? audio interface not in brief | 28.2 × 28.2 × 2.2 | ? | ? | Reject: size. No India approval listed |
| Trasna (ex-u-blox) LENA-R8001-01C | ? | 1 bis + 2G | ✅ FDD B1/3/5/8 (+2/4/7/12/20/28/66) · TDD B38/40/41 (global) | ✅ VoLTE + CSFB, **only from the "01C" version**; "00C" is call setup without audio (EOL) | ✅ I²S / PCM, 4-wire (01C only) | **30.0 × 27.0** | **3 µA** PSM deep sleep (01C) | ? | Reject: too big. The M10 variant's built-in GNSS is L1-only (no NavIC) |
| Trasna ADAM-R11 | ? | 1 bis | ✅ R11001D: B1/3/5/8 + TDD B34/38/39/40/41 | ❌ "data-only" | ❌ I²S row empty | 18.0 × 18.0 | 4 µA deep sleep | ✅ SGP.32 ready, internal eSIM option | Reject: data-only |
| Trasna LEXI-R10 | ? | 1 bis | ? not checked (no voice, so moot) | ❌ "data-only" | ❌ I²S row empty | **16 × 16** (smallest Cat 1 bis) | 2 µA hibernate · 10 µA eDRX | ✅ SGP.32 ready, LPAd | Reject: data-only. Watch for a voice variant |
| Cavli C16QS-IN-GNAH | QCX216 class | 1 bis | ✅ B1/3/5/8/40/41 | ❌ no VoLTE (confirmed by the user) | ⚠ I²S ×1 "requires SDK" | 26.5 × 22.5 × 2.3 | 11 µA hibernate | ✅ integrated eSIM | Reject: no VoLTE, and big. Indian vendor, so keep in view |
| Nordic nRF93M1-LABA | Nordic (in-house) | 1 bis (Rel 14) | ✅ LABA: FDD B1/3/5/7/8/20/28 · TDD B38/40/41 | ❌ no voice, IMS or audio anywhere in datasheet v0.7 | ❌ none (UART, USB, SIM, GPIO only) | ~17.7 × 15.8 × 2.4 LGA | ? (PSM / eDRX supported) | ✅ SGP.02 / .22 / .32 | Reject: data-only |

## Vendor coverage

Screened one vendor at a time, from that vendor's own datasheets, briefs or brochure.

| Vendor | Status | Best fit |
|---|---|---|
| Quectel (China, policy exception) | ✅ done (EG915U, EG912U, EC200U specs) | **EG915U-CN** (the only Quectel part with India bands, VoLTE, PCM and a usable size) |
| Telit Cinterion (Italy / US) | ✅ product briefs screened (ELS62, ELS63, LE910R1) | **ELS62-I**. Size and sleep current need the datasheet (Telit download zone, free registration) |
| Trasna, ex-u-blox cellular (since 2025) | ✅ data sheets screened (LENA-R8, ADAM-R11, LEXI-R10) | None. Only LENA-R8 has voice, and it is 30 × 27 mm. ADAM / LEXI are small but data-only |
| Cavli (India) | ✅ checked (the local PDF is image-only, so it was not grep-screened; no VoLTE is the user's finding) | None: no VoLTE. Re-check if Cavli adds it (Indian vendor, integrated eSIM) |
| Nordic (Norway) | ✅ nRF93M1 datasheet v0.7 screened | None: Cat 1 bis with India bands, but data-only |
| Sequans (France) | ✅ checked by the user | None: no Cat 1 bis module with VoLTE. Would be considered if VoLTE were not a gate |
| Semtech / Sierra Wireless, Murata | not screened (search closed) | Their portfolios are mostly Cat M / NB-IoT |

**Vendor search concluded on 2026-11-05.** The shortlist above is final until the vendors answer the open checks or a new part appears.

> u-blox sold its cellular IoT module business to **Trasna** (announced March 2025). The data sheets we screened are Trasna-branded, so the product line is alive; still check support and availability before choosing one.

## Recommendation

1. **Lead: Quectel EG915U-CN.** It is the only part whose own spec sheet confirms all three gates: India bands (the variant is labelled "China / India"), **VoLTE**, and a **PCM** digital audio port. It also has an analog mic input as a fallback, and an eSIM row. Its weakness is size (23.6 × 19.9 mm, about 25 % of the 46 × 39 mm footprint). Its 1.2 mA at PF = 256 fits the power budget's option (a) estimate (0.8–3.0 mA).
2. **Second source: Telit ELS62-I.** It is the only non-Quectel part with an India variant, VoLTE and PCM / I²S on paper. Its brief gives no size or sleep current, and it lists no India approval. A second source matters for supply risk, so get its datasheet.
3. **Rejected for missing VoLTE** even though they have India bands: Telit ELS63-I, Trasna ADAM-R11 / LEXI-R10, Cavli C16QS, Nordic nRF93M1. The small ones (LEXI-R10 at 16 × 16 mm, nRF93M1 at ~17.7 × 15.8 mm) are worth re-checking if their vendors add VoLTE.
4. **Rejected for size** (VoLTE and digital audio present): Quectel EC200U-CN (31 × 28) and EG912U (29 × 25), Telit LE910R1 (28 × 28), Trasna LENA-R8 (30 × 27).

**Next step:** buy an EVB for the **EG915U-CN** and run the A-04 test from the block diagram first: a VoLTE call on Jio and Airtel in Delhi with PCM audio injected into the uplink and the downlink muted. Use a test number first, then a coordinated 112 test call.

### Fallbacks if PCM fails in VoLTE calls

AD-01 assumes the MCU feeds both the announcement and the live mic audio over PCM. Two fallbacks, which can be combined:

1. **Announcement from the modem's own "audio playback".** Many Quectel modules (the "Audio playback / Audio recording" feature in brochure V8.6) can play a WAV / AMR file stored in module flash into the **call uplink**. The announcement clips from AD-02 (fixed sentence, digits, DIGIPIN symbols) would live in modem flash and be played in sequence by AT command (Q11).
   - **Pro:** simpler MCU firmware for the announcement.
   - **Con:** vendor-specific AT commands make it harder to change modems (against AD-03), clips must be queued without audible gaps, and it does **not** cover the live mic audio (FR-022), which still needs PCM or analog.
2. **Analog mic input.** If a module only passes audio properly through its analog mic input during VoLTE, the MCU can drive that input from a DAC or filtered PWM output. This costs an op-amp and some board area, and adds a little noise, but it keeps "one MEMS mic routed through the MCU".

Both are plan B. Neither is a reason to pick a module without PCM.

Note: "audio playback / recording" is **not** VoLTE. It only plays into calls the module can already make. VoLTE support is a separate row in the brochure.

## Open checks

Ask the vendors these before ordering EVBs:

| # | Question | EG915U-CN | ELS62-I |
|---|---|---|---|
| Q1 | **IMS emergency call (112) over VoLTE** works, with and without a SIM, on Jio and Airtel | ask | ask |
| Q2 | PCM audio active during a **VoLTE** call (not only CS voice). Can the downlink be muted (`AT+CMUT`-type commands)? Supported sample rates (8 / 16 kHz)? | ask | ask |
| Q3 | VoLTE profile tested on Jio / Airtel / Vi (IMS config, carrier IOT) | ask | ask |
| Q4 | **TEC MTCTE** certificate for this exact variant | ask | ask |
| Q5 | eSIM: does it support an external MFF2 eUICC? Is an SGP.32 IPA (IoT Profile Assistant) in the module firmware? | ask | ask |
| Q6 | PSM / eDRX current, and whether Indian operators grant PSM / eDRX to voice SIMs (AD-05) | ask | ask |
| Q7 | Peak current during a Tx burst (sizes the VBAT bulk capacitance and the battery C-rate) | ask | ask |
| Q8 | Chipset confirmation (EG915U is believed to be UNISOC 8910DM) | ask | ask |
| Q9 | Which **ordering code** has voice / VoLTE enabled (spec V1.8 lists VoLTE under "Voice (Optional)")? | ask | – |
| Q11 | Can the module's **audio playback** (a file from module flash) be routed **into the uplink of a VoLTE / IMS call**, including an emergency call? Which formats, and can clips be queued back to back without gaps? | ask | ask |
| Q12 | Module **size and sleep / PSM current** (not in the product brief) | – | ask |

## Sources

Local copies of vendor documents are in `hardware/datasheets/<Vendor>/` (git-ignored).

**Quectel**
- EG915U Series spec V1.8: <https://www.quectel.com/blog/document/lte-cat-1-bis-eg915u-series>
- EG912U Series spec V1.6; EC200U Series spec V1.8; Product Brochure V8.6 (local copies, from quectel.com)

**Telit Cinterion** (product briefs, local copies)
- ELS62 Series brief
- ELS63: <https://www.telit.com/wp-content/uploads/2025/06/TC_ELS63_Product_Brief.pdf> · page <https://www.telit.com/devices/els63/>
- LE910R1: <https://telit.com/wp-content/uploads/2024/11/TC_LE910R1_Product_Brief.pdf> · page <https://www.telit.com/devices/le910r1-series/>

**Nordic**
- nRF93M1 Datasheet v0.7 (local copy)

**Trasna (ex-u-blox)**
- Data sheets LENA-R8 (TRSC-437461976-63), ADAM-R11 (-98), LEXI-R10 (-60) (local copies)
- Acquisition: <https://www.iot-now.com/2025/03/18/150445-trasna-acquires-u-blox-cellular-iot-modules/>

**Cavli**
- C16QS: <https://www.cavliwireless.com/c-series/c16qs.html>, spec V2.7 <https://shop.mev-elektronik.com/wp-content/uploads/C16QS-Cat1.bis-Technical-Specification-Document-V2.7.pdf>
