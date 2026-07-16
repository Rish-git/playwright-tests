import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

new_user= {
    "name":"Rishabh singh",
    "email": "rishabh@test.com"
}

response = requests.post("https://jsonplaceholder.typicode.com/users", json=new_user, verify=False)
data = response.json()
rsp = response.status_code
try:
    assert rsp==201
    print('The status code is ', response.status_code)
except AssertionError:
    print(f'The status code has to be 201, where as the server responed {rsp}')

try:
    assert data["name"]==new_user["name"]
    print(f'Name matches: {data["name"]}')
except AssertionError:
    print(f'Mismatch - Sent: {new_user["name"]}, Got: {data["name"]}')

try:
    assert "id" in data
    print("User ID: ", data["id"])
except AssertionError:
    print("ID missing")
