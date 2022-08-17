import time
import requests
from xml.etree import ElementTree
from better_profanity import profanity
from ..rustplus_proto import AppRequest, AppResponse, AppSuccess, AppChatMessage
from .handler import RequestHandler
from ..data import MessageManager


class SendMessageHandler(RequestHandler):

    def handle(self, app_request: AppRequest) -> AppResponse:

        username = ElementTree.fromstring(
            requests.get(f"https://steamcommunity.com/profiles/{app_request.playerId}?xml=1").content)\
            .find("steamID").text

        app_message = AppChatMessage()
        app_message.steamId = app_request.playerId
        app_message.name = username
        app_message.message = profanity.censor(app_request.sendTeamMessage.message)
        app_message.color = "#FFFFFF"
        app_message.time = int(time.time())
        MessageManager.add_message(app_message)

        response = AppResponse()
        response.success.CopyFrom(AppSuccess())
        return response
