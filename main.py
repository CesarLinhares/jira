import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://lionx.atlassian.net/rest/api/3/jql/"

auth = HTTPBasicAuth("clc@lionx.com.br", "swILrfFwJTbr3InVLwVw231A")
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload = json.dumps( {
  "projectIds": [
     26,
  ],
  "includeCollapsedFields": True
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
