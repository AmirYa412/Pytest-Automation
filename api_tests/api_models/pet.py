from api_tests.support.client import Client
from jsonschema import validate


class Pet(Client):
    PATH = "/pet"

    def create_pet(self, data):
        return self.post_request(self.PATH, json=data)

    def get_pet(self, pet_id):
        return self.get_request(f"{self.PATH}/{pet_id}")


    @staticmethod
    def get_payload_data(pet_id=0, pet_name=None, category_id=0, category_name=None,
                         status=None, photo_urls=None, tag_id=0, tag_name=None):
        return {
            "id": pet_id,
            "category": {
                "id": category_id,
                "name": category_name
            },
            "name": pet_name,
            "photoUrls": [photo_urls],
            "tags": [
                {
                    "id": tag_id,
                    "name": tag_name
                }
            ],
            "status": status
        }

    @staticmethod
    def validate_pet_creation_schema(response_data):
        pet_schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "category": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"}
                    },
                    "required": ["id", "name"]
                },
                "name": {"type": "string"},
                "photoUrls": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "tags": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"}
                        },
                        "required": ["id", "name"]
                    }
                },
                "status": {
                    "type": "string",
                    "enum": ["available", "pending", "sold"]
                }
            },
            "required": ["id", "name", "photoUrls", "tags", "status"]
        }
        validate(instance=response_data, schema=pet_schema)



class PetFindByStatus(Client):
    PATH = "/pet/findByStatus"
    @staticmethod
    def get_query_params(status=None):
        return {
            "status": status
        }

    def get_pets_by_status(self, status):
        params = self.get_query_params(status=status)
        return self.get_request('/pet/findByStatus', params=params)

    @staticmethod
    def validate_results_in_expected_status(status, items):
        try:
            for pet in items:
                if pet["status"] != status:
                    return False
            return True
        except Exception as e:
            raise Exception(e)
