import pytest
from api_tests.tests.pet.api_models import Pet
from api_tests.tests.pet.api_models import PetID
from api_tests.tests.pet.api_models import PetFindByStatus

pytestmark = pytest.mark.api


@pytest.mark.usefixtures("api_test_class_setup")
class TestPet:
    def test_unauthorized_user_cant_create_pet(self):
        client = Pet(self.env)
        data = client.get_payload_data()
        response = client.post_request('/pet', data=data)
        assert response.status_code == 400
        assert response.json()["message"] == "bad input"


@pytest.mark.usefixtures("api_test_class_setup")
class TestPetID:
    def test_not_exists_id_status_code_404(self):
        client = PetID(self.env)
        response = client.get_request("/pet/invalidid")
        assert response.status_code == 404


@pytest.mark.usefixtures("api_test_class_setup")
class TestPetFindByStatus:
    @pytest.mark.parametrize("status", ["sold", "available"])
    def test_get_results_by_status(self, status):
        client = PetFindByStatus(self.env)
        params = client.get_query_params(status=status)
        response = client.get_request('/pet/findByStatus', params=params)
        assert response.status_code == 200
        response_data = response.json()
        assert client.are_results_in_expected_status(status, response_data)
