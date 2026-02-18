#!/usr/bin/env python3
"""
task_03_http_server.py

A simple API using Python's built-in http.server.
Routes:
  GET /       -> plain text greeting
  GET /data   -> JSON sample data
  GET /status -> plain text "OK"
  GET /info   -> JSON metadata
  else        -> 404 Endpoint not found
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_text(self, status_code: int, body: str) -> None:
        data = body.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_json(self, status_code: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        # Basic routing based on the request path
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/info":
            self._send_json(
                200,
                {"version": "1.0", "description": "A simple API built with http.server"},
            )
        else:
            self._send_text(404, "Endpoint not found")

    # Optional: reduce noisy default logging (comment out if you want logs)
    def log_message(self, format: str, *args) -> None:
        return


def run(host: str = "localhost", port: int = 8000) -> None:
    server = HTTPServer((host, port), SimpleAPIHandler)
    print(f"Serving on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("\nServer stopped.")


if __name__ == "__main__":
    run()
