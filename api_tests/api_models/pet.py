from requests import Response
from api_tests.support.client import Client
from jsonschema import validate

class Pet(Client):

    PATH = "/pet"

    def create_pet(self, data: dict) -> Response:
        return self.post_request(self.PATH, json=data)

    def get_pet(self, pet_id: int | str) -> Response:
        return self.get_request(f"{self.PATH}/{pet_id}")

    @staticmethod
    def get_payload_data(
        pet_id: int = 0,
        pet_name: str | None = None,
        category_id: int = 0,
        category_name: str | None = None,
        status: str | None = None,
        photo_urls: str | None = None,
        tag_id: int = 0,
        tag_name: str | None = None
    ) -> dict:
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
    def validate_pet_creation_schema(response_data: dict):
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

    @staticmethod
    def validate_error_response_schema(response_data: dict):
        """Validate API error response structure, based on status code"""
        error_schema = {
            "type": "object",
            "properties": {
                "code": {"type": "integer"},
                "type": {"type": "string"},
                "message": {"type": "string"}
            },
            "required": ["code", "type", "message"]
        }
        validate(instance=response_data, schema=error_schema)


class PetFindByStatus(Client):

    PATH = "/pet/findByStatus"

    @staticmethod
    def get_query_params(status: str | None=None) -> dict:
        return {"status": status}

    def get_pets_by_status(self, status: str) -> Response:
        """Find pets by status (available, pending, sold)."""
        params = self.get_query_params(status=status)
        return self.get_request(self.PATH, params=params)

    @staticmethod
    def validate_pet_list_schema(response_data: list):
        """Validate list of pets response structure.

        Args:
            response_data: List of pet objects from API

        Raises:
            ValidationError: If response doesn't match expected list schema
        """
        pet_list_schema = {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "status": {
                        "type": "string",
                        "enum": ["available", "pending", "sold"]
                    },
                    "photoUrls": {"type": "array"}
                },
                "required": ["id", "photoUrls", "status"]
            }
        }
        validate(instance=response_data, schema=pet_list_schema)

    @staticmethod
    def validate_results_in_expected_status(status: str, items: list[dict]) -> bool:
        try:
            for pet in items:
                if pet["status"] != status:
                    return False
            return True
        except Exception as e:
            raise Exception(e)
