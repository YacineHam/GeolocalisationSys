
import asyncio
import json
import websockets

#SECIND COMMIT

async def hello():
    uri = "ws://127.0.0.1:8000/ws/test/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMzUyNzU3OCwianRpIjoiNzZiY2EyMDA4MWE3NDZiMTg3ODkyMzFkMzk3YzNmYjciLCJ1c2VyX2lkIjoyfQ.krMbIWbofVTPdfPGw2cMrIY5zRAxuiIBpsojUkwocRU"
    async with websockets.connect(uri) as websocket:
        for i in range(10):
                    x={'car':'','longitude':10,'latitude':50}
                    message=json.dumps(x)
                    await websocket.send(message)
                    print(f"> {message}")





asyncio.get_event_loop().run_until_complete(hello())