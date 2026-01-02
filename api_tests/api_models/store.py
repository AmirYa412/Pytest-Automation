from api_tests.support.client import Client
from datetime import datetime, timezone


class StoreInventory(Client):
    PATH = "/store/inventory"

    def get_store_inventory(self):
        """Returns store inventory"""
        return self.get_request(self.PATH)


class StoreOrder(Client):
    PATH = "/store/order"

    def create_order(self, data):
        "Create a new order in the store"
        return self.post_request(self.PATH, json=data)

    @staticmethod
    def get_payload_data(order_id=None, pet_id=None, quantity=None, status=None, complete=True):
        return {

                "id": order_id,
                "petId": pet_id,
                "quantity": quantity,
                "shipDate": datetime.now(timezone.utc).isoformat(timespec='milliseconds'),
                "status": status,
                "complete": complete
        }
