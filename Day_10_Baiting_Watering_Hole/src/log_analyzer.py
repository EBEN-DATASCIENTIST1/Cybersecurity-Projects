
import json
from collections import Counter
from pathlib import Path

LOG_FILE = Path("reports/visit_log.jsonl")
OUTPUT_FILE = Path("reports/visit_analysis.json")


def main():
    if not LOG_FILE.exists():
        print("Visit log not found. Run the honeypot first.")
        return

    entries = []

    try:
        with LOG_FILE.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    entry = json.loads(line)
                    if isinstance(entry, dict):
                        entries.append(entry)
                    else:
                        print(f"Skipping invalid record on line {line_number}.")
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON on line {line_number}.")

        paths = Counter(entry.get("path", "Unknown") for entry in entries)
        agents = Counter(
            entry.get("user_agent", "Unknown") for entry in entries
        )

        analysis = {
            "total_visits": len(entries),
            "unique_paths": len(paths),
            "path_counts": dict(paths),
            "user_agent_counts": dict(agents),
            "scope": "Local honeypot simulation",
            "limitation": (
                "A recorded visit does not prove malicious intent."
            ),
        }

        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_FILE.write_text(
            json.dumps(analysis, indent=2),
            encoding="utf-8",
        )

        print(f"Total visits: {len(entries)}")
        print(f"Unique paths: {len(paths)}")
        print(f"Analysis saved to: {OUTPUT_FILE}")

    except OSError as error:
        print(f"Could not analyze visit log: {error}")


if __name__ == "__main__":
    main()
