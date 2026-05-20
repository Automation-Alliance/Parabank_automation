import requests


url = ("https://jsonplaceholder.typicode.com/posts")

data = {

    "title": "Parabank API",

    "body": "Automation Testing",

    "userId": 1
}

response = requests.post(url,json=data)

print("Status Code:",response.status_code)

print(response.json())