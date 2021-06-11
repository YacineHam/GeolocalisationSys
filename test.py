
import asyncio
import json
import websockets
import time

#SECIND COMMIT

async def hello():
    uri = "ws://127.0.0.1:8000/ws/test/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMzUyOTcwNSwianRpIjoiZDA3NzcxMDYwODMxNDY2N2FkMDM4NTQxYzYyOGI2YjYiLCJ1c2VyX2lkIjoyfQ.3GRSsEGQk--MmUwM6qXp_eok7eaB_TsDKDAtwgYn1XU"
    async with websockets.connect(uri) as websocket:
        for i in range(10):
            x={'car':'','longitude':10,'latitude':60}
            name=json.dumps(x)
            await websocket.send(name)
            print(f"> {name}")
            time.sleep(2)

asyncio.get_event_loop().run_until_complete(hello())