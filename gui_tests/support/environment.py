import os
from gui_tests.users.users import PRODUCTION_USERS, CI_USERS

GUI_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class Environment:
    def __init__(self, env_prefix, protocol=None):
        self.prefix = env_prefix
        self.protocol = protocol if protocol else "https://"
        self.domain = f"{self.prefix}.saucedemo.com"
        self.base_url = f"{self.protocol}{self.domain}"
        self.is_ci = self.is_ci_environment()
        self.users = self.get_automation_users()
        self.timeout = 10 if self.is_ci else 5

    def __repr__(self):
        return  f"<Environment prefix='{self.prefix}' base_url='{self.base_url}' is_ci={self.is_ci} timeout={self.timeout}>"

    def is_ci_environment(self):
        return self.prefix in ("qa", "dev")

    def get_automation_users(self):
        users = CI_USERS if self.is_ci else PRODUCTION_USERS
        # Validate users have passwords
        for user_key, user_data in users.items():
            if user_data.get("password") is None:
                raise ValueError(f"User '{user_key}' has None password. Check configuration in test_users/users.py")
        return users
