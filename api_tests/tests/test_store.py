from pytest import mark
from api_tests.api_models.store import StoreInventory
from api_tests.api_models.store import StoreOrder
from api_tests.support.environment import Environment

pytestmark = [mark.api, mark.store]


@mark.usefixtures("api_test_class_setup")
class TestStoreInventory:

    client : StoreInventory
    env : Environment

    def setup_method(self):
        if not hasattr(self.__class__, 'client'):
            self.__class__.client = StoreInventory(self.env)

    def teardown_method(self):
        self.client.reset_session()

    def test_get_store_inventory_data(self):
        response = self.client.get_store_inventory()
        assert response.status_code == 200
        response_data = response.json()
        self.client.validate_inventory_response_schema(response_data)


@mark.usefixtures("api_test_class_setup")
class TestStoreOrder:

    client : StoreOrder
    env : Environment

    def setup_method(self):
        if not hasattr(self.__class__, 'client'):
            self.__class__.client = StoreOrder(self.env)

    def teardown_method(self):
        self.client.reset_session()

    def test_place_new_story_order(self):
        data = self.client.get_payload_data(order_id=1, pet_id=1, quantity=1, status="placed")
        response = self.client.create_order(data=data)
        assert response.status_code == 200
        response_data = response.json()
        self.client.validate_order_response_schema(response_data)
        assert response_data["id"] == data["id"]
        assert response_data["quantity"] == data["quantity"]
        assert response_data["status"] == data["status"]


