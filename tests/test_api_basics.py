import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
'''print(response.status_code)
print(response.json())'''

data = response.json()

#assertion to check real values
try:
    assert response.status_code == 200
    print("status code checked pass")
except AssertionError:
    print("Status code check failed")

expected_name="leawne"
try:
    assert data["name"] == expected_name
    print("Name check passed")
except KeyError:
    print("❌ Name check failed - 'name' key not found in response")
except AssertionError:
    print(f"❌ Name check failed - Expected {expected_name}, Got '{data.get('name')}'")

get_id=1
try:
    assert data ["id"] == get_id
    print("ID check passed")
except KeyError:
    print("❌ ID check failed - 'ID' key not found in response")
except AssertionError:
    print(f"❌ ID check failed - Expected {get_id}, Got '{data.get('id')}'")
'''
print('All assertion passed!')
print(f"User name : {data['name']}")
print(f"User email: {data['email']}")'''
