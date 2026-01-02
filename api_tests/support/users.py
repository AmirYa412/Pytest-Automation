import os
from dotenv import load_dotenv

load_dotenv()

PRODUCTION_USERS = {
    "user_1" : {
      "name": "prod.automation_user@typicode.com",
      "password": os.getenv('PROD_USER1_PASSWORD', None)
    }
}


CI_USERS = {
    "user_1" : {
      "name": "qa.automation_user@typicode.com",
      "password": os.getenv("CI_USER1_PASSWORD", None)
    }
}