from ..rustplus_proto import AppRequest, AppResponse, AppSuccess, AppError
from .handler import RequestHandler
from ..data import TeamManager


class PromoteLeaderHandler(RequestHandler):
    def handle(self, app_request: AppRequest) -> AppResponse:

        response = AppResponse()
        if TeamManager.set_leader(
            app_request.playerId, app_request.promoteToLeader.steamId
        ):
            response.success.CopyFrom(AppSuccess())
        else:
            error = AppError()
            error.error = "SteamId not part of team"
            response.error.CopyFrom(error)
        return response
