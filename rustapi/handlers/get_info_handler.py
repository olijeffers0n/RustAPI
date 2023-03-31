import random

from ..rustplus_proto import AppRequest, AppResponse, AppInfo
from .handler import RequestHandler
import time


class GetInfoHandler(RequestHandler):
    def handle(self, app_request: AppRequest) -> AppResponse:
        response = AppResponse()
        info = AppInfo()
        info.name = "RustAPI Testing Server"
        info.headerImage = "http://test.com/"
        info.url = "http://test.com/"
        info.map = "6000 Size Procedural Map"
        info.mapSize = 6000
        info.wipeTime = int(time.time() - 60 * 60 * 24 * 5)
        info.players = random.randint(0, 200)
        info.maxPlayers = 200
        info.queuedPlayers = 0
        info.seed = 54321
        info.salt = 0
        info.logoImage = "http://test.com/"

        response.info.CopyFrom(info)
        return response
