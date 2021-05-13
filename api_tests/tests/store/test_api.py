import pytest
from api_tests.tests.store.api_models import V2StoreInventory
from api_tests.tests.store.api_models import V2StoreOrder
from api_tests.utils.custom_assert_utils import KeyAsserter

pytestmark = pytest.mark.api


@pytest.mark.usefixtures("api_test_class_setup")
class TestStoreInventory:
    def test_get_store_inventory_data(self):
        client = V2StoreInventory(self.env)
        response = client.get_request('/v2/store/inventory')
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data.keys()) > 4


@pytest.mark.usefixtures("api_test_class_setup")
class TestStoreOrder:
    def test_get_order_data_by_id(self):
        client = V2StoreOrder(self.env)
        response = client.get_request('/v2/store/order/1')
        assert response.status_code == 200
        response_data = response.json()
        KeyAsserter.verify_expected_keys_in_response_data(response_data.keys(), ["id", "status", "complete", "quantity"])
        assert response_data["id"] == 1

