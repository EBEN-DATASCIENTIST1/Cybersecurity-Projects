
import json
import platform
import socket
from datetime import datetime, timezone
from getpass import getuser
from pathlib import Path


def usb_payload_sim(output_file="reports/recon_log.json"):
    """Record basic system information for a local awareness exercise."""
    info = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "version": platform.version(),
        "user": getuser(),
        "cwd": str(Path.cwd()),
        "simulation": True,
        "network_activity": False,
    }

    report_path = Path(output_file)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        report_path.write_text(
            json.dumps(info, indent=2),
            encoding="utf-8",
        )
    except OSError as error:
        print(f"Could not save report: {error}")
        return

    print("USB drop awareness simulation completed.")
    print(f"Simulated system information saved to: {report_path}")


if __name__ == "__main__":
    usb_payload_sim()
