diff --git a/scripts/analyze_intercepts.py b/scripts/analyze_intercepts.py
new file mode 100755
index 0000000000000000000000000000000000000000..652b47eb0e7f87866d29b481c53f0ecd3dd4ffb8
--- /dev/null
+++ b/scripts/analyze_intercepts.py
@@ -0,0 +1,121 @@
+#!/usr/bin/env python3
+"""Summarize SIGINT intercept logs from the lab."""
+from __future__ import annotations
+
+import argparse
+import csv
+from collections import Counter, defaultdict
+from datetime import datetime
+from pathlib import Path
+from typing import Iterable
+
+
+SERVICE_BANDS = [
+    (87.5, 108.0, "FM Broadcast"),
+    (108.0, 117.95, "Air Navigation"),
+    (118.0, 137.0, "Airband AM"),
+    (137.0, 138.0, "Weather Satellite"),
+    (144.0, 148.0, "Amateur 2m"),
+    (156.0, 162.55, "Marine VHF"),
+    (162.4, 162.55, "NOAA Weather"),
+    (161.975, 162.025, "AIS"),
+    (420.0, 450.0, "Amateur 70cm"),
+    (1090.0, 1090.0, "ADS-B"),
+]
+
+
+def guess_service(freq_mhz: float) -> str:
+    for low, high, label in SERVICE_BANDS:
+        if low <= freq_mhz <= high:
+            return label
+    if 30.0 <= freq_mhz < 88.0:
+        return "VHF Low"
+    if 225.0 <= freq_mhz < 400.0:
+        return "Military Air"
+    if 406.0 <= freq_mhz <= 406.1:
+        return "EPIRB/ELT Beacons"
+    return "Unknown"
+
+
+def parse_timestamp(value: str) -> datetime | None:
+    value = value.strip()
+    if not value:
+        return None
+    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
+        try:
+            return datetime.strptime(value, fmt)
+        except ValueError:
+            continue
+    return None
+
+
+def normalize(value: str) -> str:
+    return value.strip() if value else ""
+
+
+def load_rows(path: Path) -> Iterable[dict[str, str]]:
+    with path.open(newline="", encoding="utf-8") as handle:
+        reader = csv.DictReader(handle)
+        for row in reader:
+            yield {key: normalize(val) for key, val in row.items()}
+
+
+def summarize(rows: Iterable[dict[str, str]]) -> dict[str, Counter]:
+    counters: dict[str, Counter] = defaultdict(Counter)
+    for row in rows:
+        freq = row.get("frequency_mhz", "")
+        service = row.get("service", "")
+        modulation = row.get("modulation", "")
+        classification = row.get("classification", "")
+        timestamp = row.get("timestamp", "")
+
+        if freq:
+            try:
+                freq_mhz = float(freq)
+            except ValueError:
+                freq_mhz = 0.0
+            if not service:
+                service = guess_service(freq_mhz)
+            counters["frequency"][f"{freq_mhz:.3f} MHz"] += 1
+            counters["band"][guess_service(freq_mhz)] += 1
+
+        if service:
+            counters["service"][service] += 1
+        if modulation:
+            counters["modulation"][modulation] += 1
+        if classification:
+            counters["classification"][classification] += 1
+
+        parsed = parse_timestamp(timestamp)
+        if parsed:
+            counters["date"][parsed.strftime("%Y-%m-%d")] += 1
+
+    return counters
+
+
+def print_counter(title: str, counter: Counter, limit: int | None = None) -> None:
+    print(f"\n{title}")
+    print("-" * len(title))
+    for key, value in counter.most_common(limit):
+        print(f"{key:30s} {value:>3d}")
+
+
+def main() -> None:
+    parser = argparse.ArgumentParser(description="Summarize intercept log CSV files.")
+    parser.add_argument("csv_file", type=Path, help="Path to intercept log CSV")
+    parser.add_argument("--top", type=int, default=10, help="Top N frequencies to show")
+    args = parser.parse_args()
+
+    rows = list(load_rows(args.csv_file))
+    counters = summarize(rows)
+
+    print(f"Total intercepts: {len(rows)}")
+    print_counter("By Service", counters["service"])
+    print_counter("By Modulation", counters["modulation"])
+    print_counter("By Classification", counters["classification"])
+    print_counter("By Date", counters["date"])
+    print_counter("Top Frequencies", counters["frequency"], limit=args.top)
+
+
+if __name__ == "__main__":
+    main()
