import requests

URL = "https://httpbin.org/encoding/utf8"

result = requests.get(URL)

print(result.text)
