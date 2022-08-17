import json
import random
import time

from ..rustplus_proto import AppChatMessage


def init_message_data() -> dict:
    with open("./rustapi/data/messages.json", "r") as message_data:
        return json.load(message_data)


class Utils:

    _message_data: dict = init_message_data()

    @staticmethod
    def chance(percentage: float) -> bool:
        return random.random() < percentage / 100

    @staticmethod
    def generate_chat_message(message: str = None) -> AppChatMessage:

        user = random.choice(Utils._message_data["users"])
        steam_id = user["id"]
        name = user["name"]

        if message is None:
            message = random.choice(Utils._message_data["messages"])

        chat = AppChatMessage()
        chat.steamId = steam_id
        chat.name = name
        chat.message = message
        chat.color = "#FFFFFF"
        chat.time = int(time.time())

        return chat
