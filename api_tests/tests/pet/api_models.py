from api_tests.core.set_client import ClientSession
import json


class V2Pet(ClientSession):
    """
    Path:   /v2/pet
    """

    @staticmethod
    def get_payload_data(pet_id=None, category_id=None, category_name=None, pet_name=None, photo_url=None, tag_id=None, tag_name=None, status=None):
        return {
                  "id": pet_id,
                  "category": json.dumps({"id": category_id, "name": category_name}),
                  "name": pet_name,
                  "photoUrls": json.dumps([photo_url]),
                  "tags": json.dumps([{"id": tag_id, "name": tag_name}]),
                  "status": status
                }


class V2PetID(ClientSession):
    """
    Path:   /v2/pet/<PET_ID>
    """


class V2PetFindbystatus(ClientSession):
    """
    Path:   /v2/pet/findByStatus
    """
    @staticmethod
    def get_query_params(status=None):
        return {
            "status": status
        }

    @staticmethod
    def are_results_in_expected_status(status, items):
        try:
            for pet in items:
                if pet["status"] != status:
                    return False
            return True
        except Exception as e:
            raise Exception(e)
