# WebSockets

This project introduces asynchronous real-time communication using Python, `asyncio`, the `websockets` library, and ASGI with Starlette and Uvicorn.

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
| 3. Unicast | `unicast_server.py` | WebSocket server tracking `connected_clients` and replying only to the sender with `U:` |
| 4. Broadcast | `broadcast_server.py` | WebSocket server broadcasting incoming messages prefixed with `B:` to all connected clients |
| 5. ASGI Integration | `asgi_server.py` | Starlette ASGI app serving HTTP on `/` and WebSocket echo on `/ws` via Uvicorn |
