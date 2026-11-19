#!/usr/bin/env python3
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def broadcast(message: str) -> None:
    if not connected_clients:
        return
    payload = f"B:{message}"
    targets = list(connected_clients)
    await asyncio.gather(
        *(client.send(payload) for client in targets),
        return_exceptions=True
    )


async def connection_handler(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            if isinstance(message, str):
                await broadcast(message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
