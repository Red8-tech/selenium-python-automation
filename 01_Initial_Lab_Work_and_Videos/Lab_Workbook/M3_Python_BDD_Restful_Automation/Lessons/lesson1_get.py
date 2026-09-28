import requests


url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print("Status code:", response.status_code)
print("Headers:", response.headers)


data = response.json()

print("ID:", data["id"])
print("Title:", data["title"])

assert response.status_code == 200
assert data["id"] == 1

print("GET request test passed")
