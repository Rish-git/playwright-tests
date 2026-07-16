import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

updated_user = {
    "name": "Rishabh Updated",
    "email": "rishabh_new@test.com"
}

response = requests.put("https://jsonplaceholder.typicode.com/users/1", json=updated_user, verify=False)
data = response.json()
rsp = response.status_code
print(rsp)
print(data)

try:
    assert rsp==200
    print('The status code is ', rsp)
except AssertionError:
    print(f'The status code has to be 201, where as the server responed {rsp}')

try:
    assert data["name"]==updated_user["name"]
    print(f'Name matches: {data["name"]}')
except AssertionError:
    print(f'Mismatch - Sent: {updated_user["name"]}, Got: {data["name"]}')

try:
    assert data["id"] == 1
    print("User ID:", data["id"])
except AssertionError:
    print(f"Expected ID 1, but got {data['id']}")
except KeyError:
    print("ID missing")