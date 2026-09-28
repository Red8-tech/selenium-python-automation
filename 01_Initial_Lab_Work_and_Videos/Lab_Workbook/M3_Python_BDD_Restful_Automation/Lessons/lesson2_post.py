import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My First API Test",
    "body": "Learning POST request with Python",
    "userId": 1
}


headers = {
    "Content-Type": "application/json"
}


response = requests.post(
    url,
    json=payload,
    headers=headers
)


print("Status Code:", response.status_code)
print("Response:", response.json())


assert response.status_code == 201


print("POST request test passed")
