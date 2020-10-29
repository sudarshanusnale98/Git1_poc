import requests
from pprint import pprint
from scret import Token_Value

API_URL = "https://api.github.com"
GITHUB_TOKEN = Token_Value
payload = '{"name" = "TestName"}'
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}

def userProject():
    p = requests.post(API_URL + "/user/projects", data='{"name":"New_user_Proj"}', headers=headers)
    pprint(p.json())


