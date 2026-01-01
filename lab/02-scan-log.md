diff --git a/lab/02-scan-log.md b/lab/02-scan-log.md
new file mode 100644
index 0000000000000000000000000000000000000000..5ed01d12e22c88814406b185e81b3ffa389410d9
--- /dev/null
+++ b/lab/02-scan-log.md
@@ -0,0 +1,24 @@
+# Lab 02 — Band Scanning & Logging
+
+## Objective
+Conduct a structured sweep across multiple bands and record intercept metadata.
+
+## Procedure
+1. Pick **three bands** to cover (ex: NOAA, airband, AIS).
+2. Scan for 10–15 minutes per band.
+3. For each intercept, log:
+   - Timestamp
+   - Frequency (MHz)
+   - Modulation
+   - Service (if known)
+   - Classification (COMINT/ELINT)
+   - Signal strength (RSSI or S-meter)
+   - Notes (brief description)
+
+## Logging Tips
+- Use **short, objective descriptions** ("ATIS airport loop", "AIS burst").
+- If unsure of a service, leave blank and classify later.
+- Capture screenshots of waterfall or spectrum if helpful.
+
+## Exit Criteria
+A minimum of **10 distinct intercepts** across at least **three** services.
