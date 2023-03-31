class LimitedList:
    def __init__(self, size: int) -> None:
        self.data = []
        self.size = size

    def add(self, element) -> None:
        if len(self.data) == self.size:
            self.data.pop(0)
        self.data.append(element)

    def get(self) -> list:
        return self.data


class MessageManager:

    _messages = LimitedList(15)

    @staticmethod
    def add_message(message: str) -> None:
        MessageManager._messages.add(message)

    @staticmethod
    def get_messages() -> list:
        return MessageManager._messages.get()
