import base64
from websocket import WebSocket
from rustapi.rustplus_proto import AppRequest, AppEmpty, AppResponse, AppMessage

ws = WebSocket()
ws.connect("ws://localhost:4565")

request = AppRequest()
request.seq = 1
request.playerId = 7892387
request.playerToken = 6732762
request.getMap.CopyFrom(AppEmpty())
ws.send(base64.b64encode(request.SerializeToString()))
data = base64.b64decode(ws.recv())
print(data)
resp = AppMessage()
resp.ParseFromString(data)
print(resp)

