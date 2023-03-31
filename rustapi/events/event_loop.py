import threading
import time
from ..utils import Utils
from .event_broadcaster import EventBroadcaster


class RustEventLoop:
    def __init__(self):
        self.thread = None

    @staticmethod
    def _run() -> None:
        while True:

            if Utils.chance(40):
                chat_message = Utils.generate_chat_message()
                EventBroadcaster.broadcast_team_chat(chat_message)

            if Utils.chance(10):
                # TODO: Team changed broadcast
                pass

            if Utils.chance(20):
                # TODO: Entity update message
                pass

            time.sleep(5)

    def start(self) -> None:
        self.thread = threading.Thread(target=RustEventLoop._run, daemon=True)
        self.thread.start()
