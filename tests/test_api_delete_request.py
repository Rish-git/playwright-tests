import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.delete("https://jsonplaceholder.typicode.com/users/1", verify=False)

print(response.status_code)
print(response.json())

try:
    assert response.status_code == 200
    print("Delete successful, status:", response.status_code)
except AssertionError:
    print(f"Delete failed - Expected 200, Got {response.status_code}")