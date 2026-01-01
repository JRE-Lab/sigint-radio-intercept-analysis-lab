diff --git a/lab/01-setup.md b/lab/01-setup.md
new file mode 100644
index 0000000000000000000000000000000000000000..db391e0bdebecb6b9e02a69b7d3cf8e7952c2d58
--- /dev/null
+++ b/lab/01-setup.md
@@ -0,0 +1,35 @@
+# Lab 01 — Equipment Setup & Calibration
+
+## Hardware
+- RTL-SDR (or equivalent SDR receiver)
+- Antenna suited to VHF/UHF (telescopic whip or discone)
+- Optional: antenna tripod or window mount
+
+## Software
+- SDR software: SDR++ or GQRX
+- Decoder tools (optional):
+  - `dump1090` or ADS-B Exchange feeders for 1090 MHz
+  - `aisdecoder` for AIS
+  - `multimon-ng` for common digital protocols
+
+## Calibration Checklist
+1. **Install drivers** for your SDR dongle.
+2. **Verify reception** by tuning to a local FM broadcast station.
+3. **Set PPM correction** if known (use known carriers for reference).
+4. **Record baseline noise floor** for your environment.
+
+## Quick Start Frequencies
+| Band | Frequency (MHz) | Notes |
+| --- | --- | --- |
+| FM Broadcast | 88-108 | Strong signals for calibration |
+| NOAA Weather | 162.4-162.55 | Continuous voice loop |
+| Airband | 118-137 | AM modulation |
+| AIS | 161.975 / 162.025 | Maritime position packets |
+| ADS-B | 1090 | Aircraft transponder bursts |
+
+## Logging Setup
+Copy the template and start logging:
+
+```bash
+cp templates/intercept_log.csv data/my_intercepts.csv
+```
