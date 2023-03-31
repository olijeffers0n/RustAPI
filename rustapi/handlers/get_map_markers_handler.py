from ..rustplus_proto import AppRequest, AppResponse, AppMapMarkers, AppMarker, Vector4
from .handler import RequestHandler
from ..utils import Utils
import json


class GetMapMarkersHandler(RequestHandler):
    def __init__(self):
        with open("./rustapi/data/markers.json", "r") as f:
            data = json.load(f)

        self.id = 1
        self.launch = (data["launchsite"]["x"], data["launchsite"]["y"])

        self.crates = []
        for crate_data in data["crates"]:
            self.crates.append((crate_data["x"], crate_data["y"]))

        self.vending_machines = []
        for vending_machine_data in data["vending_machines"]:
            marker = AppMarker()
            marker.id = self.id
            self.id += 1
            marker.type = 3
            marker.x = vending_machine_data["x"]
            marker.y = vending_machine_data["y"]
            marker.name = vending_machine_data["name"]
            marker.outOfStock = (
                False if len(vending_machine_data["sell_orders"]) == 0 else True
            )
            marker.sellOrders.extend(
                [
                    AppMarker.SellOrder(
                        itemId=order["item_id"],
                        quantity=order["quantity"],
                        currencyId=order["currency_id"],
                        costPerItem=order["cost_per_item"],
                        amountInStock=order["amount_in_stock"],
                        itemIsBlueprint=order["item_is_blueprint"],
                        currencyIsBlueprint=order["currency_is_blueprint"],
                    )
                    for order in vending_machine_data["sell_orders"]
                ]
            )
            self.vending_machines.append(marker)

    def handle(self, app_request: AppRequest) -> AppResponse:

        # First we must construct the response
        response = AppResponse()
        # Now we need to add the markers to the response
        markers = AppMapMarkers()
        marker_list = [elem for elem in self.vending_machines]

        for crate in self.crates:
            if Utils.chance(40):
                marker = AppMarker()
                marker.id = self.id
                self.id += 1
                marker.type = 6
                marker.x = crate[0]
                marker.y = crate[1]
                marker_list.append(marker)

        # TODO: Add Helicopter, Chinook and Launch site explosion markers

        markers.markers.extend(marker_list)
        response.mapMarkers.CopyFrom(markers)
        return response
