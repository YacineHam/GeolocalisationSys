
import asyncio
import json
import websockets
import time

#SECIND COMMIT

async def hello():
    uri = "ws://127.0.0.1:8000/ws/test/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMzUzMDg5MywianRpIjoiZjMzZDFmNTI3NDY0NDg1MTkwZTBkNDZjZjk0ZTUyYjkiLCJ1c2VyX2lkIjozfQ.ZxaBHxc8UwjHt45uRNQVvgB_XP79SZk2R6LUY-GVu1Q"
    async with websockets.connect(uri) as websocket:
        for i in range(10):
            x={'car':'','longitude':1,'latitude':1}
            name=json.dumps(x)
            await websocket.send(name)
            print(f"> {name}")
            time.sleep(2)

asyncio.get_event_loop().run_until_complete(hello())