diff --git a/scripts/validate_intercepts.py b/scripts/validate_intercepts.py
new file mode 100755
index 0000000000000000000000000000000000000000..4f49fdba36f5add5e87654aae565b293d674b2ec
--- /dev/null
+++ b/scripts/validate_intercepts.py
@@ -0,0 +1,93 @@
+#!/usr/bin/env python3
+"""Validate SIGINT intercept logs for required fields and formatting."""
+from __future__ import annotations
+
+import argparse
+import csv
+from datetime import datetime
+from pathlib import Path
+
+REQUIRED_COLUMNS = [
+    "timestamp",
+    "frequency_mhz",
+    "modulation",
+    "service",
+    "classification",
+    "rssi_dbm",
+    "notes",
+]
+
+ALLOWED_CLASSIFICATIONS = {"COMINT", "ELINT"}
+
+
+def parse_timestamp(value: str) -> bool:
+    if not value:
+        return False
+    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
+        try:
+            datetime.strptime(value, fmt)
+            return True
+        except ValueError:
+            continue
+    return False
+
+
+def validate_row(row: dict[str, str], line_no: int) -> list[str]:
+    errors: list[str] = []
+    timestamp = row.get("timestamp", "").strip()
+    if not parse_timestamp(timestamp):
+        errors.append(f"Line {line_no}: invalid timestamp '{timestamp}'")
+
+    freq = row.get("frequency_mhz", "").strip()
+    try:
+        freq_value = float(freq)
+        if freq_value <= 0:
+            errors.append(f"Line {line_no}: frequency must be positive")
+    except ValueError:
+        errors.append(f"Line {line_no}: invalid frequency '{freq}'")
+
+    classification = row.get("classification", "").strip().upper()
+    if classification and classification not in ALLOWED_CLASSIFICATIONS:
+        errors.append(
+            f"Line {line_no}: classification '{classification}' must be COMINT or ELINT"
+        )
+
+    rssi = row.get("rssi_dbm", "").strip()
+    if rssi:
+        try:
+            float(rssi)
+        except ValueError:
+            errors.append(f"Line {line_no}: invalid rssi_dbm '{rssi}'")
+
+    return errors
+
+
+def validate_csv(path: Path) -> list[str]:
+    errors: list[str] = []
+    with path.open(newline="", encoding="utf-8") as handle:
+        reader = csv.DictReader(handle)
+        missing = [col for col in REQUIRED_COLUMNS if col not in reader.fieldnames]
+        if missing:
+            return [f"Missing columns: {', '.join(missing)}"]
+        for line_no, row in enumerate(reader, start=2):
+            errors.extend(validate_row(row, line_no))
+    return errors
+
+
+def main() -> None:
+    parser = argparse.ArgumentParser(description="Validate intercept CSV format.")
+    parser.add_argument("csv_file", type=Path, help="Path to intercept log CSV")
+    args = parser.parse_args()
+
+    errors = validate_csv(args.csv_file)
+    if errors:
+        print("Validation errors:")
+        for error in errors:
+            print(f"- {error}")
+        raise SystemExit(1)
+
+    print("Validation passed: no issues found.")
+
+
+if __name__ == "__main__":
+    main()
