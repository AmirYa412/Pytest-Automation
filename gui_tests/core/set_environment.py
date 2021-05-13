import os
import json

_home_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class TestedEnvironment:
    def __init__(self, env_prefix, protocol=None):
        self.prefix = env_prefix
        self.protocol = protocol if protocol else "https://"
        self.host = self.protocol + self.prefix + ".saucedemo.com"
        self.users = self.get_automation_users()

    def is_sandbox_env(self):
        return self.prefix in ("qa", "dev")

    def get_automation_users(self):
        users_file_name = "qa_test_users.json"
        if self.prefix in ("www", "staging"):
            users_file_name = "prod_test_users.json"
        elif self.prefix in ("dev", "dev2"):
            users_file_name = "dev_test_users.json"

        with open(os.path.join(_home_path, 'test_users', users_file_name)) as users_file:
            users = json.loads(users_file.read())
        return users
