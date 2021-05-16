import pytest
from api_tests.tests.pet.api_models import V2Pet
from api_tests.tests.pet.api_models import V2PetID
from api_tests.tests.pet.api_models import V2PetFindbystatus

pytestmark = pytest.mark.api


@pytest.mark.usefixtures("api_test_class_setup")
class TestPet:
    def test_unauthorized_user_cant_create_pet(self):
        client = V2Pet(self.env)
        data = client.get_payload_data()
        response = client.post_request('/v2/pet', data=data)
        assert response.status_code == 400
        assert response.json()["message"] == "bad input"


@pytest.mark.usefixtures("api_test_class_setup")
class TestPetID:
    def test_get_pet_by_id(self):
        status = "available"
        params = V2PetFindbystatus.get_query_params(status=status)
        client = V2PetID(self.env)
        response = client.get_request('/v2/pet/findByStatus', params=params)
        assert response.status_code == 200
        pet_id = response.json()[0]["id"]
        response = client.get_request("/v2/pet/%s" % pet_id)
        assert response.status_code == 200
        assert response.json()["id"] == pet_id


@pytest.mark.usefixtures("api_test_class_setup")
class TestPetFindByStatus:
    @pytest.mark.parametrize("status", ["sold", "available"])
    def test_get_results_by_status(self, status):
        client = V2PetFindbystatus(self.env)
        params = client.get_query_params(status=status)
        response = client.get_request('/v2/pet/findByStatus', params=params)
        assert response.status_code == 200
        response_data = response.json()
        assert client.are_results_in_expected_status(status, response_data)


