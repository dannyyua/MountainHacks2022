import asyncio
import websockets

# connect to this socket with python -m websockets ws://142.58.168.251:8765/

socks = set()

async def echo(websocket):
    async for message in websocket:
        if (websocket not in socks):
            socks.add(websocket)

        for ws in socks:
            if (ws != websocket):     
                await ws.send(message)
    

async def main():
    async with websockets.serve(echo, "142.58.168.251", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())