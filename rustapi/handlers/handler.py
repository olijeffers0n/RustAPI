from ..rustplus_proto import AppRequest, AppResponse


class RequestHandler:

    def handle(self, app_request: AppRequest) -> AppResponse:
        pass
