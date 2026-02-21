#!/usr/bin/env python3
import argparse
import csv
import json
import pathlib


def infer_schema(csv_path: pathlib.Path) -> list[dict[str, str]]:
    with csv_path.open(newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
    return [{"name": field, "type": "string"} for field in fields]


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate dataset ingestion starter spec")
    parser.add_argument("--csv", required=True)
    ns = parser.parse_args()

    path = pathlib.Path(ns.csv)
    schema = infer_schema(path)
    payload = {
        "source": str(path),
        "schema": schema,
        "pipeline_steps": ["extract", "validate", "load", "quality_report"],
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
