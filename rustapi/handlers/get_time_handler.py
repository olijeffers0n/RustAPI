import random

from ..rustplus_proto import AppRequest, AppResponse, AppTime
from .handler import RequestHandler


class GetTimeHandler(RequestHandler):
    def handle(self, app_request: AppRequest) -> AppResponse:
        response = AppResponse()
        time = AppTime()

        time.dayLengthMinutes = 60
        time.timeScale = 1
        time.sunrise = 7.34114695
        time.sunset = 19.7066727
        time.time = random.randint(5, 240000000) / 10000000

        response.time.CopyFrom(time)
        return response
