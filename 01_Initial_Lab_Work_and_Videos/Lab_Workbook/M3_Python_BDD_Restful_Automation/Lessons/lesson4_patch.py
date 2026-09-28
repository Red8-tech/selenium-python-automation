# Change only the fields I provide.

import requests


url = "https://jsonplaceholder.typicode.com/posts/1"


payload = {
    "title": "Only Title Changed"
}


response = requests.patch(url, json=payload)

print("PATCH Status Code:", response.status_code)
print("PATCH Response:", response.json())


assert response.status_code == 200

print("PATCH request test passed")
