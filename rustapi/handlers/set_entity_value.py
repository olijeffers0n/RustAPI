from ..rustplus_proto import AppRequest, AppResponse, AppSuccess
from .handler import RequestHandler
from ..data import EntityManager


class SetEntityValueHandler(RequestHandler):

    def __init__(self):
        self.entity_manager = EntityManager()

    def handle(self, app_request: AppRequest) -> AppResponse:
        response = AppResponse()
        self.entity_manager.get_or_create_entity(app_request.entityId, False, app_request.setEntityValue.value)
        response.success.CopyFrom(AppSuccess())
        return response
