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

def updateProject():
    update = requests.patch(API_URL + "/projects/5775782", data='{"name":"Testing_1"}', headers=headers)
    pprint(update.json())


