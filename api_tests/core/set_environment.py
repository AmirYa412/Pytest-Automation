import os
import json

_home_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class TestedEnvironment:
    def __init__(self, env_prefix):
        self.env_prefix = env_prefix
        self.protocol = "https://"
        self.host = self.env_prefix + ".swagger.io/v2"
        self.is_sandbox_env = True if env_prefix in ("qa", "dev") else False
        self.headers = self.set_env_headers()
        self.users = self.get_automation_users()

    def is_sandbox_env(self):
        return self.env_prefix in ("qa", "dev")

    def set_env_headers(self):
        try:
            return {
                "Accept": "application/json",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9,",
                "Connection": "keep-alive",
                "Host": "{}.swagger.io".format(self.env_prefix),
                "Origin": "https://{}.swagger.io".format(self.env_prefix),
                "Referer": "https://{}.swagger.io/".format(self.env_prefix),
                "Content-Type": "application/json; charset=utf-8",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Upgrade-Insecure-Requests": "1"
            }
        except BaseException as e:
            raise BaseException(e)

    def get_automation_users(self):
        users_file_name = "qa_test_users.json"
        if self.env_prefix in ("www", "staging", "petstore"):
            users_file_name = "prod_test_users.json"
        elif self.env_prefix in ("dev", "dev2"):
            users_file_name = "dev_test_users.jsvon"

        with open(os.path.join(_home_path, 'test_users', users_file_name)) as users_file:
            users = json.loads(users_file.read())
        return users
