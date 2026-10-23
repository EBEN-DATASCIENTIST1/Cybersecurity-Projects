
import json
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

HOST = "127.0.0.1"
PORT = 8080
LOG_FILE = Path("reports/visit_log.jsonl")


class HoneyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Record only requests from the local computer.
        if self.client_address[0] not in ("127.0.0.1", "::1"):
            self.send_error(403, "Local testing only")
            return

        entry = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "client_ip": self.client_address[0],
            "path": self.path,
            "user_agent": self.headers.get("User-Agent", "Unknown"),
        }

        try:
            LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
            with LOG_FILE.open("a", encoding="utf-8") as file:
                file.write(json.dumps(entry) + "\n")
        except OSError:
            self.send_error(500, "Could not write visit log")
            return

        print(json.dumps(entry))

        body = (
            b"Local honeypot simulation. "
            b"No file was downloaded or executed."
        )
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format_string, *args):
        # Avoid duplicate default HTTP access logs.
        pass


if __name__ == "__main__":
    print(f"Local honeypot running at http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop.")
    HTTPServer((HOST, PORT), HoneyHandler).serve_forever()
