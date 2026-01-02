from pytest import mark
from api_tests.api_models.store import StoreInventory
from api_tests.api_models.store import StoreOrder

pytestmark = mark.api


@mark.usefixtures("api_test_class_setup")
class TestStoreInventory:
    client : StoreInventory
    def setup_method(self):
        if not hasattr(self.__class__, 'client'):
            self.__class__.client = StoreInventory(self.env)

    def teardown_method(self):
        self.client.reset_session()

    def test_get_store_inventory_data(self):
        response = self.client.get_store_inventory()
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data.keys()) > 0


@mark.usefixtures("api_test_class_setup")
class TestStoreOrder:
    client : StoreOrder
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
        assert response_data["id"] == data["id"]
        assert response_data["quantity"] == data["quantity"]
        assert response_data["status"] == data["status"]


