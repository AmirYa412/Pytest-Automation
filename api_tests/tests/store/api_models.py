from api_tests.core.set_client import ClientSession
from datetime import datetime


class V2StoreInventory(ClientSession):
    """
    Path:   /v2/store/inventory
    """


class V2StoreOrder(ClientSession):
    """
    Path: /v2/store/order
    Path: /v2/store/order/<ORDER_ID>
    """
    @staticmethod
    def get_payload_data(id=None, pet_id=None, quantity=None, status=None, complete=True):
        return {

                "id": id,
                "petId": pet_id,
                "quantity": quantity,
                "shipDate": str(datetime.strftime(datetime.now(), "%y-%m-%dT%H:%M%SSSZ")),
                "status": status,
                "complete": complete

        }
