import requests

url = "http://localhost:8000/invoke"

response = requests.post(url, json={"message": "Você ainda lembra meu nome?"})

print(response.content)