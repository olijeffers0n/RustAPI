from websocket import WebSocket
from rustapi.rustplus_proto import AppRequest, AppEmpty, AppResponse

ws = WebSocket()
ws.connect("ws://localhost:4565")

request = AppRequest()
request.seq = 1
request.playerId = 7892387
request.playerToken = 6732762
request.getInfo.CopyFrom(AppEmpty())
print(request)
ws.send_binary(request.SerializeToString())
data = ws.recv()
print(data)
resp = AppResponse()
resp.ParseFromString(data)
print(resp)

