diff --git a/lab/04-decode.md b/lab/04-decode.md
new file mode 100644
index 0000000000000000000000000000000000000000..f4fca4324cbfec6fb113494645f4351f7d03914a
--- /dev/null
+++ b/lab/04-decode.md
@@ -0,0 +1,19 @@
+# Lab 04 — Decode Unencrypted Digital Signals
+
+## Objective
+Decode at least one unencrypted protocol to extract structured information.
+
+## Suggested Targets
+- **ADS-B (1090 MHz):** aircraft positions and identifiers.
+- **AIS (161.975/162.025 MHz):** vessel positions and MMSI.
+- **ACARS (131.525 MHz):** aircraft short text messages (if unencrypted).
+
+## Procedure
+1. Configure your decoder (dump1090, aisdecoder, multimon-ng).
+2. Verify that decodes are valid.
+3. Capture a short sample of decoded output.
+4. Record metadata in the intercept log.
+
+## Output Checklist
+- Screenshot or log snippet of decoded output.
+- Notes about what the decoded data implies (e.g., traffic density, aircraft routes).
