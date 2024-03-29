import json

from ..rustplus_proto import AppRequest, AppResponse, AppMap
from .handler import RequestHandler


class GetMapHandler(RequestHandler):
    def __init__(self):
        with open("./rustapi/data/map.png", "rb") as image:
            f = image.read()
            self.map = bytes(bytearray(f))

        self.monuments = []

        with open("./rustapi/data/monuments.json", "r") as monuments:
            mons = json.load(monuments)
            for mon in mons:
                monument = AppMap.Monument()
                monument.token = mon["token"]
                monument.x = mon["x"]
                monument.y = mon["y"]
                self.monuments.append(monument)

        self.response = AppResponse()
        map_data = AppMap()

        map_data.width = 4000
        map_data.height = 4000
        map_data.jpgImage = self.map
        map_data.oceanMargin = 500
        map_data.monuments.extend(self.monuments)
        map_data.background = "#12404D"

        self.response.map.CopyFrom(map_data)

    def handle(self, app_request: AppRequest) -> AppResponse:

        return self.response
