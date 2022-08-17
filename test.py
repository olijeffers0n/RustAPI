import base64
from websocket import WebSocket
from rustapi.rustplus_proto import AppRequest, AppEmpty, AppResponse, AppMessage, AppSendMessage

ws = WebSocket()
ws.connect("ws://localhost:4565")

request = AppRequest()
request.seq = 1
request.playerId = 76561198438796495
request.playerToken = 6732762

send = AppSendMessage()
send.message = "fuck World slag bitches"
request.sendTeamMessage.CopyFrom(send)
ws.send(base64.b64encode(request.SerializeToString()))

data = base64.b64decode(ws.recv())
print(data)
resp = AppMessage()
resp.ParseFromString(data)
print(resp)

request = AppRequest()
request.seq = 2
request.playerId = 76561198438796495
request.playerToken = 6732762

request.getTeamChat.CopyFrom(AppEmpty())
ws.send(base64.b64encode(request.SerializeToString()))

data = base64.b64decode(ws.recv())
print(data)
resp = AppMessage()
resp.ParseFromString(data)
print(resp)

#import requests, json
#from bs4 import BeautifulSoup
#
#data = {
#    "users": []
#}
#
#for i in range(300):
#    try:
#        id = 76561198438796495+i
#        page = requests.get(f"https://steamcommunity.com/profiles/{id}")
#        # Parse the page with bs4 and the name is in the span of class actual_persona_name
#        soup = BeautifulSoup(page.text, "lxml")
#        name = soup.find(class_="actual_persona_name").text
#        print(name)
#        data["users"].append({"id": id, "name": name})
#    except Exception as e:
#        print(e)
#
#with open("users.json", "w") as f:
#    json.dump(data, f)

