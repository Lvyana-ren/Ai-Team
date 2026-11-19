# Skill: Android & Kernel Engineering

## Preflight facts
- Device codename and SoC
- Android version/API and target ROM
- ABI and vendor interface
- Kernel source/base/version and defconfig
- Toolchain and build environment
- Boot image/partition format and recovery path

## High-risk areas
DTB/DTBO, boot/vendor_boot/init_boot, AVB, partition sizing, charging, thermal, regulator, clock, memory, scheduler, and power management.

## Rules
- Trace behavior to source, logs, or reproducible evidence.
- Do not infer undocumented register behavior.
- Preserve a known-good boot/recovery path.
- Separate build success from physical-device validation.
- State exactly which hardware/ROM combinations were tested.
