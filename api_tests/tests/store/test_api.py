import pytest
from api_tests.tests.store.api_models import StoreInventory
from api_tests.tests.store.api_models import StoreOrder

pytestmark = pytest.mark.api


@pytest.mark.usefixtures("api_test_class_setup")
class TestStoreInventory:
    def test_get_store_inventory_data(self):
        client = StoreInventory(self.env)
        response = client.get_request('/v2/store/inventory')
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data.keys()) > 4


@pytest.mark.usefixtures("api_test_class_setup")
class TestStoreOrder:
    def test_get_order_data_by_id(self):
        client = StoreOrder(self.env)
        response = client.get_request('/v2/store/order/1')
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["id"] == 1
        assert response_data["complete"] is True

