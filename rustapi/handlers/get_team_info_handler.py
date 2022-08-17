from .handler import RequestHandler
from ..rustplus_proto import AppRequest, AppResponse
from ..data import TeamManager


class GetTeamInfoHandler(RequestHandler):

    def handle(self, app_request: AppRequest) -> AppResponse:
        response = AppResponse()
        response.teamInfo.CopyFrom(TeamManager.get_team_info())
        return response
