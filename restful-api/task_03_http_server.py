#!/usr/bin/env python3
"""
task_03_http_server.py
A simple API using Python's built-in http.server module.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_text(self, status_code: int, body: str) -> None:
        """Send a plain text response."""
        encoded = body.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def _send_json(self, status_code: int, payload: dict) -> None:
        """Send a JSON response."""
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        # Basic routing by path
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/status":
            self._send_text(200, "OK")
        else:
            self._send_text(404, "Endpoint not found")

    def log_message(self, format: str, *args) -> None:
        """
        Optional: keep default logging quiet/clean.
        Comment this out if you want normal request logs.
        """
        return


def run(host: str = "0.0.0.0", port: int = 8000) -> None:
    server = HTTPServer((host, port), SimpleAPIHandler)
    print(f"Serving simple API on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("\nServer stopped.")


if __name__ == "__main__":
    run()
