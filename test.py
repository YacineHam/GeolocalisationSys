
import asyncio
import json
import websockets

#SECIND COMMIT

async def hello():
    uri = "ws://127.0.0.1:8000/ws/test/"
    async with websockets.connect(uri) as websocket:
        x={'car':'','longitude':10,'latitude':100}
        name=json.dumps(x)
        await websocket.send(name)
        print(f"> {name}")

asyncio.get_event_loop().run_until_complete(hello())