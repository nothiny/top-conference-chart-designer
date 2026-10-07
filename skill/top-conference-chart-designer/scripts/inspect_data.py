"""Profile a tabular input without changing it.

Usage:
    python inspect_data.py --input results.csv --out figure_output/input_profile.json

CSV/TSV/JSON use the standard library. XLSX and Parquet use pandas when it is
available. The report is a planning aid, not a substitute for understanding
the experiment's semantics.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from typing import Any


MISSING = {"", "na", "n/a", "nan", "null", "none", "-"}


def parse_number(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip()
    if text.lower() in MISSING:
        return None
    try:
        number = float(text)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def read_rows(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix in {".csv", ".tsv"}:
        delimiter = "\t" if suffix == ".tsv" else ","
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return [dict(row) for row in csv.DictReader(handle)]
    if suffix == ".json":
        value = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(value, dict):
            for key in ("data", "rows", "records"):
                if isinstance(value.get(key), list):
                    value = value[key]
                    break
        if not isinstance(value, list) or not all(isinstance(row, dict) for row in value):
            raise ValueError("JSON must be a list of objects or contain data/rows/records")
        return [dict(row) for row in value]
    try:
        import pandas as pd
    except ImportError as exc:
        raise RuntimeError("XLSX/Parquet input requires pandas") from exc
    frame = pd.read_excel(path) if suffix in {".xlsx", ".xls"} else pd.read_parquet(path)
    return frame.where(frame.notna(), None).to_dict(orient="records")


def profile(path: Path) -> dict[str, Any]:
    rows = read_rows(path)
    columns = sorted({str(key) for row in rows for key in row})
    fields: dict[str, Any] = {}
    for column in columns:
        values = [row.get(column) for row in rows]
        present = [value for value in values if value is not None and str(value).strip().lower() not in MISSING]
        numbers = [number for value in present if (number := parse_number(value)) is not None]
        numeric = bool(present) and len(numbers) == len(present)
        unique = {str(value) for value in present}
        fields[column] = {
            "inferred_type": "numeric" if numeric else "categorical",
            "missing_count": len(values) - len(present),
            "unique_count": len(unique),
            "examples": list(sorted(unique))[:8],
        }
        if numeric:
            fields[column]["min"] = min(numbers)
            fields[column]["max"] = max(numbers)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        "input": str(path.resolve()),
        "sha256": digest,
        "row_count": len(rows),
        "columns": columns,
        "fields": fields,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    report = profile(args.input)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
