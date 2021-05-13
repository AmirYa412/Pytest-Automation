import pytest
from api_tests.tests.random_joke.api_models import Random_Joke


@pytest.mark.usefixtures("api_test_class_setup")
class TestRandomJoke:
    def test_get_random_joke_response_200(self):
        client = Random_Joke(self.env)
        response = client.get_request('/random_joke')
        assert response.status_code == 200
