import requests


class ClientSession:
    def __init__(self, env, user=None):
        self.domain = env.protocol + env.host
        self.users = env.users
        self.host = env.host
        self.session = requests.Session()
        self.session.headers.update(env.headers)
        if user:    # Login if user supplied
            self.auth_user(user)

    def get_request(self, path, params=None, data=None):
        response = self.session.get(self.domain + path, params=params, data=data, verify=False)
        return response

    def post_request(self, path, params=None, data=None, files=None):
        response = self.session.post(self.domain + path, params=params, data=data, files=files, verify=False)
        return response

    def auth_user(self, user):
        try:
            auth_data = self.users[user]
            response = self.post_request("/auth", data=auth_data)
            return response
        except Exception as e:
            raise Exception("Could not auth user to %s, against %s env ERROR:%s" % (self.users[user], self.domain, e))