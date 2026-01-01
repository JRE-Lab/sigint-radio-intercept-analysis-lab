diff --git a/lab/03-classify.md b/lab/03-classify.md
new file mode 100644
index 0000000000000000000000000000000000000000..645b6a44bf9bef4b515f151e038613c9ed073d2b
--- /dev/null
+++ b/lab/03-classify.md
@@ -0,0 +1,23 @@
+# Lab 03 — Signal Classification
+
+## Objective
+Classify each intercept and attach contextual meaning.
+
+## Classification Guidelines
+- **COMINT** if the signal carries human or machine communication.
+- **ELINT** if the signal is a beacon, telemetry, or other non-communication emission.
+
+## Rapid Service Identification
+Use frequency ranges as anchors:
+- 162.4–162.55 MHz: NOAA Weather
+- 118–137 MHz: Airband AM
+- 161.975 / 162.025 MHz: AIS
+- 1090 MHz: ADS-B (Mode S)
+- 144–148 MHz / 420–450 MHz: Amateur Radio
+
+## Task
+1. Update your log with service and classification.
+2. Add a short confidence note (High/Medium/Low) in the notes column.
+
+## Exit Criteria
+All log entries have service and classification fields populated.
