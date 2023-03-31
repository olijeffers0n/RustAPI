from ..rustplus_proto import AppRequest, AppResponse, AppEntityInfo
from .handler import RequestHandler
from ..data import EntityManager


class GetEntityInfoHandler(RequestHandler):
    def __init__(self):
        self.entity_manager = EntityManager()

    def handle(self, app_request: AppRequest) -> AppResponse:
        response = AppResponse()
        entity_info = AppEntityInfo(
            type=app_request.entityId % 3 + 1,
            payload=self.entity_manager.get_or_create_entity(
                app_request.entityId, True
            ),
        )
        response.entityInfo.CopyFrom(entity_info)
        return response
