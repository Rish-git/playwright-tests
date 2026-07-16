import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

users_to_create = [
    {"name": "Rishabh Singh", "email": "rishabh@test.com"},
    {"name": "John Doe", "email": "john@test.com"},
    {"name": "Jane Smith", "email": "jane@test.com"},
]
for user in users_to_create:
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=user, verify=False)
    data = response.json()
    rsp = response.status_code
    print(f"Created: {data['name']} - Status: {rsp}")
    
    try:
        assert rsp==201
        print('The status code is ', rsp)
    except AssertionError:
        print(f'The status code has to be 201, where as the server responed {rsp}')
        
    try:
        assert data["name"]==user["name"]
        print(f'Name matches: {data["name"]}')
    except AssertionError:
        print(f'Mismatch - Sent: {user["name"]}, Got: {data["name"]}')
        
    try:
        assert "id" in data
        print("User ID: ", data["id"])
    except AssertionError:
        print("ID missing")
