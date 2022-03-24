# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://lionx.atlassian.net/rest/api/3/issuetype"

auth = HTTPBasicAuth("clc@lionx.com.br", "swILrfFwJTbr3InVLwVw231A")

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
print(len(json.dumps(json.loads(response.text), sort_keys=False, indent=4, separators=(",", ": "))))
print(json.dumps(json.loads(response.text), sort_keys=False, indent=4, separators=(",", ": ")))
