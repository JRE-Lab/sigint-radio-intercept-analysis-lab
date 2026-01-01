diff --git a/lab/00-overview.md b/lab/00-overview.md
new file mode 100644
index 0000000000000000000000000000000000000000..dae16d3a835d19fdf13ce88b5a273508608d507d
--- /dev/null
+++ b/lab/00-overview.md
@@ -0,0 +1,26 @@
+# Lab 00 — Mission Overview
+
+## Objective
+Build practical SIGINT tradecraft by locating, logging, classifying, and analyzing **unencrypted** radio transmissions. This lab focuses on lawful intercepts and disciplined documentation.
+
+## Lab Flow
+1. Prepare your SDR, antenna, and logging tools.
+2. Sweep multiple bands and record intercept metadata.
+3. Classify each intercept (COMINT vs ELINT) and tag likely services.
+4. Decode unencrypted digital protocols where possible.
+5. Analyze patterns and write a concise intelligence summary.
+
+## Key Definitions
+- **COMINT:** Communications intelligence derived from human or machine communications.
+- **ELINT:** Electronic intelligence derived from non-communication signals (beacons, radar, telemetry).
+- **Intercept Record:** A structured log entry containing the time, frequency, modulation, and context of a signal.
+
+## Deliverables
+- Completed intercept log (CSV).
+- One-page analysis memo summarizing findings.
+- Optional: decoded captures (screenshots, demodulated audio, or packet logs).
+
+## Legal/Ethical Guardrails
+- Only intercept **public, unencrypted** transmissions.
+- Do not share personal or sensitive details from any intercepted content.
+- Follow local laws and SDR equipment regulations.
