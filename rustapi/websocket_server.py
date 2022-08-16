import logging
from wsocket import WSocketApp, run
from .rustplus_proto import AppMessage, AppRequest, AppResponse, AppError
from .handlers import RequestHandler, GetInfoHandler


class RustAPIWebsocketServer:

    def __init__(self):
        self.server = None
        self.fields = {
            "getInfo": GetInfoHandler(),
            "getTime": None,
            "getMap": None,
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

    def on_message_received(self, message, client):
        try:
            request = AppRequest()
            request.ParseFromString(message)
            handler = self.convert_message_to_handler(message)
            response = handler.handle(request)

        except Exception as e:
            response = AppResponse()
            error = AppError()
            error.error = str(e)
            response.error.CopyFrom(error)

        response.seq = 1
        message = AppMessage()
        message.response.CopyFrom(response)
        return message.SerializeToString()

    def start(self):
        self.server = WSocketApp()
        self.server.onmessage += self.on_message_received
        run(app=self.server, port=4565)
