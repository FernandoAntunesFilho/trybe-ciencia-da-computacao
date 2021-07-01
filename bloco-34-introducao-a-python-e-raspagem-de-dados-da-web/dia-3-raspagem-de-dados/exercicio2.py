import requests
import json

URL = "https://api.github.com/users"

response = requests.get(URL)
git_users = json.loads(response.text)

for user in git_users:
    login = user["login"]
    url = user["url"]
    print(login, url)
