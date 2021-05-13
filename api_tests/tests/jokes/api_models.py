from api_tests.core.set_client import ClientSession


class JokesRandom(ClientSession):
    """
    Path:   /jokes/random
    """

    @staticmethod
    def get_query_params(joke_id=None, user_id=None):
        return {
            "joke_id": joke_id,
            "user_id": user_id,
        }

    @staticmethod
    def get_payload_data(joke_title=None, joke_type=None, joke_setup=None, joke_punchline=None):
        return {
            "joke_title": joke_title,
            "joke_type": joke_type,
            "joke_setup": joke_setup,
            "joke_punchline": joke_punchline,
        }


class JokesTen(ClientSession):
    """
    Path:   /jokes/ten
    """
    @staticmethod
    def get_query_params(type=None):
        return {
            "type": type
        }

    @staticmethod
    def verify_items_ordered_by_id(items):
        for i in range(len(items)):
            if items[i]["id"] > items[i+1]["id"]:
                assert False
