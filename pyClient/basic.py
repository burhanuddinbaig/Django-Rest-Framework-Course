import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json = {"title": "Abc123", "content" : "Hello Word", "price" : "abc1234"})

# get_response = requests.get(endpoint, params = {"abc": 123}, json = {"query":"Hello Word"}) # HTTP Request

# print(get_response.headers)
print(get_response.text) # Print Raw Text Response

# print(get_response.json())  # returns json

# print(get_response.status_code)  # returns response status