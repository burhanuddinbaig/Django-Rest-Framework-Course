import requests
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done"
}

get_response = requests.post(endpoint)
print(get_response.json())  # returns json