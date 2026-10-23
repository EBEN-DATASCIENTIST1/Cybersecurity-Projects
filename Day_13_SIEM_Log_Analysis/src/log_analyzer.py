
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("data/sample_logs.txt")
REPORT_FILE = Path("reports/siem_alerts.json")

LOG_PATTERN = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(?P<event>[A-Z_]+) "
    r"user=(?P<user>\S+)"
    r"(?: ip=(?P<ip>\S+))?"
    r"(?: rule=(?P<rule>\S+))?"
)


def analyze_logs(lines):
    alerts = []
    failed_by_user = Counter()
    failed_by_ip = Counter()
    parsed_events = []

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()

        if not line:
            continue

        match = LOG_PATTERN.fullmatch(line)

        if not match:
            alerts.append({
                "type": "MALFORMED_LOG",
                "severity": "LOW",
                "line": line_number,
                "message": "Log entry does not match the expected format.",
            })
            continue

        event = match.groupdict()

        try:
            datetime.strptime(
                event["timestamp"], "%Y-%m-%d %H:%M:%S"
            )
        except ValueError:
            alerts.append({
                "type": "INVALID_TIMESTAMP",
                "severity": "LOW",
                "line": line_number,
                "message": "Log entry contains an invalid timestamp.",
            })
            continue

        event_type = event["event"]
        parsed_events.append(event)

        if event_type == "FAILED_LOGIN":
            failed_by_user[event["user"]] += 1

            if event.get("ip"):
                failed_by_ip[event["ip"]] += 1

        elif event_type == "EMAIL_RULE_CREATED":
            alerts.append({
                "type": "EMAIL_RULE_CREATED",
                "severity": "HIGH",
                "user": event["user"],
                "rule": event.get("rule") or "unknown",
                "message": (
                    "Review this email rule for unauthorized "
                    "forwarding or inbox manipulation."
                ),
            })

    for user, count in failed_by_user.items():
        if count >= 3:
            alerts.append({
                "type": "REPEATED_FAILED_LOGINS",
                "severity": "HIGH",
                "user": user,
                "count": count,
                "message": (
                    "Three or more failed login events detected "
                    "for this user."
                ),
            })

    for ip, count in failed_by_ip.items():
        if count >= 3:
            alerts.append({
                "type": "REPEATED_FAILED_LOGINS_FROM_IP",
                "severity": "HIGH",
                "ip": ip,
                "count": count,
                "message": (
                    "Three or more failed login events detected "
                    "from this IP address."
                ),
            })

    summary = {
        "total_parsed_events": len(parsed_events),
        "failed_logins": sum(
            event["event"] == "FAILED_LOGIN"
            for event in parsed_events
        ),
        "successful_logins": sum(
            event["event"] == "SUCCESS_LOGIN"
            for event in parsed_events
        ),
        "email_rules_created": sum(
            event["event"] == "EMAIL_RULE_CREATED"
            for event in parsed_events
        ),
        "alerts": alerts,
    }

    return summary


def main():
    try:
        lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
        report = analyze_logs(lines)

        REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
        REPORT_FILE.write_text(
            json.dumps(report, indent=2),
            encoding="utf-8",
        )

    except OSError as error:
        print(f"Could not read logs or save the report: {error}")
        return

    print("SIEM LOG ANALYSIS")
    print("-" * 30)
    print(f"Parsed events: {report['total_parsed_events']}")
    print(f"Failed logins: {report['failed_logins']}")
    print(f"Successful logins: {report['successful_logins']}")
    print(f"Email rules created: {report['email_rules_created']}")
    print(f"Alerts generated: {len(report['alerts'])}")

    for alert in report["alerts"]:
        print(
            f"[{alert['severity']}] "
            f"{alert['type']}: {alert['message']}"
        )

    print(f"\nReport saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()
