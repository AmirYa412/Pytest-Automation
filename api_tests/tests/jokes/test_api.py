import pytest
from api_tests.tests.jokes.api_models import JokesRandom
from api_tests.tests.jokes.api_models import JokesTen

pytestmark = pytest.mark.api


@pytest.mark.usefixtures("api_test_class_setup")
class TestJokes:
    def test_get_random_joke_response_200(self):
        client = JokesRandom(self.env)
        response = client.get_request('/jokes/random')
        assert response.status_code == 200

    @pytest.mark.parametrize("path", ["programming", "food"])
    def test_invalid_endoint_response_404(self, path):
        client = JokesRandom(self.env)
        response = client.get_request('/jokes/random/%s' % path)
        assert response.status_code == 404


@pytest.mark.usefixtures("api_test_class_setup")
class TestJokesTen:
    def test_get_10_jokes(self):
        client = JokesTen(self.env)
        params = client.get_query_params(type="programming")
        response = client.get_request('/jokes/ten', params=params)
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data) == 10


