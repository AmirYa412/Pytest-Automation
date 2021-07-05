import pytest
from api_tests.tests.store.api_models import StoreInventory
from api_tests.tests.store.api_models import StoreOrder

pytestmark = pytest.mark.api


@pytest.mark.usefixtures("api_test_class_setup")
class TestStoreInventory:
    def test_get_store_inventory_data(self):
        client = StoreInventory(self.env)
        response = client.get_request('/store/inventory')
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data.keys()) > 0


@pytest.mark.usefixtures("api_test_class_setup")
class TestStoreOrder:
    def test_block_invalid_order_creation(self):
        client = StoreOrder(self.env)
        data = client.get_payload_data(id="-1", pet_id="123", quantity="-10", status="sold")
        response = client.post_request('/store/order/', data=data)
        assert response.status_code == 400
        assert response.json()["message"] == "bad input"


