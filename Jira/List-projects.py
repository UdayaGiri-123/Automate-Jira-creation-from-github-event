# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://gsnugiri.atlassian.net/rest/api/3/project"
APITOKEN = "ATATT3xFfGF0_VeEDA5PIlsjGPp81V1yaGMz3yXIX19uVmTdLYbP78y-Oo7S3m7RxUhU9M0z37gZ_yNFqoOrP0wGB0KJ7cgHJbJzndiD62PhNsLeb7I5AyqTwvYsIOfacAN3ewU4Oph46x7wv-beZf0pzh5Gh44WIYxDhjIEoNJgqx1h9R_zH1U=0D1DA5C1"

auth = HTTPBasicAuth("gsnugiri@gmail.com", APITOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
name = output[0]["name"]
print(name)