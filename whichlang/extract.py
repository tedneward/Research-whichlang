import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--results", type=str, default=str(ROOT / "results" / "runs.jsonl"))
    p.add_argument("--out", type=str, default=str(ROOT / "extractions"))
    p.add_argument("--models", type=str, default="", help="comma-separated model ids; empty = all")
    p.add_argument("--tasks", type=str, default="", help="comma-separated task ids; empty = all")
    args = p.parse_args(argv)

    rows = _read_jsonl(Path(args.results))
    if not rows:
        print("no results to report — run `python3 -m whichlang.run` first.", file=sys.stderr)
        return 1
    for row in rows:
        extractiondir = Path(args.out) 
        model = row["model_id"]
        task = row["task_id"]
        idx = str(row["sample_idx"])

        if args.models and model not in args.models.split(","):
            continue
        if args.tasks and task not in args.tasks.split(","):
            continue

        os.makedirs(extractiondir / model / task, exist_ok=True)
        with open(extractiondir / model / task / f"response-{idx}.md", "w") as f:
            if row["response"] != None:
                f.write(row["response"])
    return 0

if __name__ == "__main__":
    sys.exit(main())
