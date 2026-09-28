# Replace/update the resource with the provided representation.

import requests


url = "https://jsonplaceholder.typicode.com/posts/1"


payload = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated Body",
    "userId": 1
}


response = requests.put(url, json=payload)


print("PUT Status Code:", response.status_code)
print("PUT Response:", response.json())


assert response.status_code == 200

print("PUT request test passed")
