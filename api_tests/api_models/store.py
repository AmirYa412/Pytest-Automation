from jsonschema import validate
from requests import Response
from api_tests.support.client import Client
from datetime import datetime, timezone


class StoreInventory(Client):

    PATH = "/store/inventory"

    def get_store_inventory(self) -> Response:
        return self.get_request(self.PATH)

    @staticmethod
    def validate_inventory_response_schema(response_data: dict):
        """Validate store inventory response structure.

        Args:
            response_data: Inventory response with status counts

        Raises:
            ValidationError: If response doesn't match expected schema
        """
        inventory_schema = {
            "type": "object",
            "additionalProperties": {"type": "integer"}  # Dynamic keys, all values must be integers
        }
        validate(instance=response_data, schema=inventory_schema)


class StoreOrder(Client):

    PATH = "/store/order"

    def create_order(self, data: dict) -> Response:
        return self.post_request(self.PATH, json=data)

    @staticmethod
    def get_payload_data(
        order_id: int | None = None,
        pet_id: int | None = None,
        quantity: int | None = None,
        status: str | None = None,
        complete: bool = True
    ) -> dict:
        return {

                "id": order_id,
                "petId": pet_id,
                "quantity": quantity,
                "shipDate": datetime.now(timezone.utc).isoformat(timespec='milliseconds'),
                "status": status,
                "complete": complete
        }

    @staticmethod
    def validate_order_response_schema(response_data: dict):
        """Validate order creation response structure.

        Args:
            response_data: Order response from API

        Raises:
            ValidationError: If response doesn't match expected schema
        """
        order_schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "petId": {"type": "integer"},
                "quantity": {"type": "integer"},
                "shipDate": {"type": "string"},
                "status": {"type": "string"},
                "complete": {"type": "boolean"}
            },
            "required": ["id", "petId", "quantity", "status", "complete"]
        }
        validate(instance=response_data, schema=order_schema)
