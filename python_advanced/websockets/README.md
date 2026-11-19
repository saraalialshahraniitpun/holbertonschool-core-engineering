# WebSockets

This project introduces asynchronous real-time communication using Python, `asyncio`, and the `websockets` library.

## Requirements
* First line of all Python files: `#!/usr/bin/env python3`
* All files must end with a new line
* Code must follow PEP8 style guidelines
* Use `websockets` and `async / await`

## Tasks

| Task | File | Description |
|---|---|---|
| 0. Server | `echo_server.py` | Asynchronous WebSocket echo server listening on `127.0.0.1:8765` |
| 1. Client | `ws_client.py` | Asynchronous WebSocket client with `connect_and_send` and CLI entry point |
| 2. Validation | `validation_server.py` | WebSocket server validating non-empty messages and handling disconnections cleanly |
