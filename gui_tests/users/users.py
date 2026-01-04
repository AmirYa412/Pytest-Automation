import os
from dotenv import load_dotenv
load_dotenv()


PRODUCTION_USER_PASS = os.getenv('PROD_SAUCEDEMO_USER_PASSWORD', None)
CI_USER_PASS = os.getenv('CI_SAUCEDEMO_USER_PASSWORD', None)


PRODUCTION_USERS = {
    "standard_user" : {
      "username": "standard_user",
      "password": PRODUCTION_USER_PASS
    },
    "locked_out_user" : {
      "username": "locked_out_user",
      "password": PRODUCTION_USER_PASS
    },
    "problem_user" : {
      "username": "problem_user",
      "password": PRODUCTION_USER_PASS
    },
    "invalid_user" : {
      "username": "invalid username",
      "password": PRODUCTION_USER_PASS
    }
}


CI_USERS = {
    "standard_user" : {
      "username": "standard_user",
      "password": CI_USER_PASS
    },
    "locked_out_user" : {
      "username": "locked_out_user",
      "password": CI_USER_PASS
    },
    "problem_user" : {
      "username": "problem_user",
      "password": CI_USER_PASS
    },
    "invalid_user" : {
      "username": "invalid username",
      "password": CI_USER_PASS
    }
}