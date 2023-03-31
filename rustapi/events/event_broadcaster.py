import base64

from websocket_server import WebsocketServer
from ..rustplus_proto import AppChatMessage, AppMessage, AppBroadcast, AppTeamMessage


class EventBroadcaster:

    _instance: WebsocketServer = None

    @staticmethod
    def set_instance(instance) -> None:
        EventBroadcaster._instance = instance

    @staticmethod
    def broadcast_team_chat(message: AppChatMessage) -> None:
        if EventBroadcaster._instance is None:
            return

        chat = AppTeamMessage()
        chat.message.CopyFrom(message)

        broadcast = AppBroadcast()
        broadcast.teamMessage.CopyFrom(chat)

        app_message = AppMessage()
        app_message.broadcast.CopyFrom(broadcast)

        EventBroadcaster._instance.send_message_to_all(
            base64.b64encode(app_message.SerializeToString())
        )
