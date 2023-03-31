from ..rustplus_proto import AppRequest, AppResponse, AppTeamChat
from .handler import RequestHandler
from ..data import MessageManager


class GetTeamChatHandler(RequestHandler):
    def handle(self, app_request: AppRequest) -> AppResponse:
        response = AppResponse()
        chat = AppTeamChat()
        chat.messages.extend(MessageManager.get_messages())

        response.teamChat.CopyFrom(chat)
        return response
