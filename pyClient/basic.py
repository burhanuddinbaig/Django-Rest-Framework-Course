import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json = {"title": "Abc123", "content" : "Hello Word", "price" : "abc1234"})

print(get_response.text) # Print Raw Text Response