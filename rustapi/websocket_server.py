import logging
import base64
from websocket_server import WebsocketServer
from .rustplus_proto import AppMessage, AppRequest, AppResponse, AppError
from .handlers import RequestHandler, GetInfoHandler, GetTimeHandler, GetMapHandler


class RustAPIWebsocketServer:

    def __init__(self):
        self.server = None
        self.fields = {
            "getInfo": GetInfoHandler(),
            "getTime": GetTimeHandler(),
            "getMap": GetMapHandler(),
            "getTeamInfo": None,
            "getTeamChat": None,
            "sendTeamMessage": None,
            "getEntityInfo": None,
            "setEntityValue": None,
            "getMapMarkers": None,
            "promoteToLeader": None
        }

    def convert_message_to_handler(self, message: AppRequest) -> RequestHandler:
        for k, v in self.fields.items():
            if message.HasField(k):
                return v

        raise Exception("Handler not found")

    def on_message_received(self, client, server, message):
        message = base64.b64decode(message)
        try:
            request = AppRequest()
            request.ParseFromString(message)
            handler = self.convert_message_to_handler(request)
            response = handler.handle(request)

        except Exception as e:
            print(e)
            response = AppResponse()
            error = AppError()
            error.error = str(e)
            response.error.CopyFrom(error)

        response.seq = 1
        message = AppMessage()
        message.response.CopyFrom(response)
        server.send_message(client, base64.b64encode(message.SerializeToString()))

    def start(self):
        self.server = WebsocketServer(port=4565, loglevel=logging.INFO)
        self.server.set_fn_message_received(self.on_message_received)
        self.server.run_forever()
