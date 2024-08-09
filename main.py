import process.heat as heat
from requests.auth import HTTPBasicAuth
from requests import post, get

# get auth token
print("enter username: ")
username = input()
print("enter password: ")
password = input()
print("enter api key: ")
api_key = input()
token_response = post("https://api.fastfieldforms.com/services/v3/authenticate",auth=HTTPBasicAuth(username, password), headers={"fastfield-api-key": api_key})
token = token_response.json().get("sessionToken")

# fetch property json
print("enter submission id: ")
submission_id = input()
property_response = get(f"https://api.fastfieldforms.com/services/v3/formresults/submission/{submission_id}",headers={'X-Gatekeeper-SessionToken': token, "fastfield-api-key": api_key})
property_data = property_response.json()


# process property json
heat_elegibility04 = heat.get_eligibility04(property_data)
print(heat_elegibility04)

