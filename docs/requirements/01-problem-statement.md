# 01 · Problem Statement

Status: `draft`

## Problem

A woman facing harassment, assault, abduction or a medical emergency in an Indian city often **cannot reach help quickly**:

- Her phone may be in a bag, snatched, or out of battery, or she may be unable to unlock it.
- Under threat or after a fall, she may be **unable to act deliberately** (dial, press, speak).
- Even when help is called, responders may **not know where she is** or where she is being taken.

## Mission

> A small, standalone wearable that **detects an emergency and silently places a VoLTE call to 112**. The call announces that it is an automated Padma SOS distress call and gives the location, then opens the microphone so the operator can hear what is happening and decide what to do. No smartphone is needed.

It is also a **tiny, reflashable LTE + GNSS + microphone platform** that others can reprogram for other ways of helping people in need.

## Initial market

- **India**, starting with metropolitan areas: **Delhi NCR** first, then **Hyderabad**.
- Emergency path: **112 / Emergency Response Support System (ERSS)**.

## Why existing options fall short

| Option | Gap |
|---|---|
| Smartphone panic button (mandated on phones sold in India) / 112 India app | Needs the phone at hand, charged and operable; requires a deliberate action |
| Safety apps (e.g. state police apps) | Same phone dependence; many alert family rather than responders |
| BLE safety pendants / keychains | Relay through the phone, so they fail if the phone is gone |
| Standalone GPS trackers (kids / elderly / vehicle AIS-140) | Bulky, manual button only, or report to a private app or portal rather than 112 |

## What makes Padma different

1. **Standalone:** its own cellular link and multi-constellation GNSS (including **NavIC**).
2. **Automatic detection:** on-device speech / scream recognition (motion detection optional), with a discreet cancel window.
3. **Silent:** no siren or audible countdown, so an attacker isn't alerted and doesn't find and discard the device.
4. **Responder-first:** a live listen-in voice call to 112, not an app notification.
5. **Wearable size:** no larger than a smartwatch case; worn as a pendant or patch.
6. **Open and reflashable:** auditable hardware and firmware that owners can reprogram.

## Success looks like (v1)

- From an automatic or manual trigger to a connected 112 call in which the operator hears the announcement, location and live audio, **reliably and in under ~60 s** including the cancel window.
- The wearer actually wears it daily: small, light, and charged once every few days or less often.
