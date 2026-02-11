#!/usr/bin/env python3
"""
task_04_net.py

Client-Server Application with Serialization (Advanced)

- The client sends a Python dictionary to the server.
- The server receives JSON-serialized data, deserializes it back into a dict,
  prints it, then closes the connection.

This implementation is designed to work with the provided testing script:
- start_server() accepts exactly ONE client connection and then exits,
  so server_thread.join() completes.
"""

import socket
import json


HOST = "127.0.0.1"
PORT = 65432
RECV_CHUNK_SIZE = 4096


def start_server(host: str = HOST, port: int = PORT) -> None:
    """
    Start a simple TCP server that accepts one connection, receives JSON data,
    deserializes it into a Python dictionary, prints it, and exits.
    """
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Helps avoid "Address already in use" during quick restarts in development.
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_sock.bind((host, port))
        server_sock.listen(1)

        conn, addr = server_sock.accept()
        with conn:
            # Read until the client closes its sending side (or closes the socket).
            chunks = []
            while True:
                data = conn.recv(RECV_CHUNK_SIZE)
                if not data:
                    break
                chunks.append(data)

            raw = b"".join(chunks).decode("utf-8")

            try:
                received_dict = json.loads(raw)
            except json.JSONDecodeError as e:
                print("Failed to decode JSON from client:", e)
                return

            print("Received Dictionary from Client:")
            print(received_dict)

    except OSError as e:
        print("Server socket error:", e)
    finally:
        server_sock.close()


def send_data(data_dict: dict, host: str = HOST, port: int = PORT) -> None:
    """
    Connect to the server, JSON-serialize the provided dictionary, send it,
    and close the connection.
    """
    try:
        serialized = json.dumps(data_dict).encode("utf-8")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
            client_sock.connect((host, port))
            client_sock.sendall(serialized)

            # Signal to the server we're done sending (so its recv loop can end).
            try:
                client_sock.shutdown(socket.SHUT_WR)
            except OSError:
                # Not fatal; connection might already be closing.
                pass

    except (ConnectionRefusedError, TimeoutError, OSError) as e:
        print("Client connection/send error:", e)
