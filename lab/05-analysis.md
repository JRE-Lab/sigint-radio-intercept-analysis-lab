diff --git a/lab/05-analysis.md b/lab/05-analysis.md
new file mode 100644
index 0000000000000000000000000000000000000000..45640c763aeedf046bacf3c16e940e7be3f885ab
--- /dev/null
+++ b/lab/05-analysis.md
@@ -0,0 +1,24 @@
+# Lab 05 — Analysis & Pattern Finding
+
+## Objective
+Identify activity patterns from your intercept log.
+
+## Automated Summary
+Use the helper script to summarize your log.
+
+```bash
+python3 scripts/analyze_intercepts.py data/my_intercepts.csv
+```
+
+## Questions to Answer
+- Which services were most active?
+- What times of day produced the most intercepts?
+- Are there frequency clusters that suggest repeaters or scheduled broadcasts?
+
+## Manual Analysis Suggestions
+- Plot intercept counts by hour (spreadsheet or Python).
+- Compare intercepts to public schedules (ATIS, marine traffic reports).
+- Look for anomalous or rare signals that deserve a deeper look.
+
+## Exit Criteria
+At least **three insights** documented in your analysis memo.
