from pytest import mark, fixture
from api_tests.api_models.pet import Pet
from api_tests.api_models.pet import PetFindByStatus

pytestmark = mark.api


@mark.usefixtures("api_test_class_setup")
class TestPet:
    client : Pet
    def setup_method(self):
        if not hasattr(self.__class__, 'client'):
            self.__class__.client = Pet(self.env)

    def teardown_method(self):
        self.client.reset_session()


    def test_new_pet_creation(self):
        data = self.client.get_payload_data(pet_id=123, pet_name="Luci", category_id=2, category_name="Dogs",
                                       status="available", tag_id=2, tag_name="Cute", photo_urls="dummy")
        response = self.client.create_pet(data)
        assert response.status_code == 200
        response_data = response.json()
        self.client.validate_pet_creation_schema(response_data)
        assert response.json() == data

    def test_create_and_get_new_pet(self):
        data = self.client.get_payload_data(pet_id=456, pet_name="Trix", category_id=4, category_name="Dogs",
                                       status="available", tag_id=2, tag_name="Fluff", photo_urls="dummy")
        self.client.create_pet(data)

        response = self.client.get_pet(456)
        assert response.status_code == 200
        response_data = response.json()
        self.client.validate_pet_creation_schema(response_data)
        assert response_data == data

    def test_get_by_invalid_pet_id_error_404(self):
        response = self.client.get_pet("InvalidID")
        assert response.status_code == 404


@mark.usefixtures("api_test_class_setup")
class TestPetFindByStatus:
    client : PetFindByStatus
    def setup_method(self):
        if not hasattr(self.__class__, 'client'):
            self.__class__.client = PetFindByStatus(self.env)

    def teardown_method(self):
        self.client.reset_session()

    @mark.parametrize("status", ["sold", "available"])
    def test_get_pets_by_status(self, status):
        response = self.client.get_pets_by_status(status)
        assert response.status_code == 200
        response_data = response.json()
        assert self.client.validate_results_in_expected_status(status, response_data)
