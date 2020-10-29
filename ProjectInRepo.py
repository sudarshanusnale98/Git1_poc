import requests
from pprint import pprint
API_URL = "https://api.github.com"
GITHUB_TOKEN = "20b4170bd537ad180c1d95e7c0d6bdf8d5e547c8"
payload = '{"name" = "TestName"}'
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}
#p = requests.post(API_URL+"/user/repos", data='{"name":"Testing_Again"}', headers=headers)
#pprint(p.json())

q = requests.post(API_URL+"/repos/preranaagale/poc/projects", data='{"name":"Testing_Again"}', headers=headers)
pprint(q.json())

#r = requests.get(API_URL+"/users/preranaagale/projects", headers=headers)

#pprint(r.json())
