
import asyncio
import json
import websockets
import time

#SECIND COMMIT

async def hello():
    uri = "ws://127.0.0.1:8000/ws/test/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI1MDk3ODk3LCJqdGkiOiIzMGQ1ZjhmM2U0MmE0ZTc2YTI0ZmMzMGEyMjE4MGM4YSIsInVzZXJfaWQiOjZ9.qXES4VBAl-A_bepEc220Q-m0Rv3MVtzXasyywep2oeA"
    async with websockets.connect(uri) as websocket:
        for i in range(10):
            x={'car':'','longitude':10,'latitude':60}
            name=json.dumps(x)
            await websocket.send(name)
            print(f"> {name}")
            time.sleep(5)

asyncio.get_event_loop().run_until_complete(hello())