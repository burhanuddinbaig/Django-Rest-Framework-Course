import requests
endpoint = "http://localhost:8000/api/products/"

headers = {'Authorization': 'Bearer 9dcd3b7044b1b47b057bb0f9f00fa8abd1ec2e05'}

data = {
    "title": "This field is done",
    "price": "32.49"
}

get_response = requests.post( endpoint, json = data, headers = headers )
print(get_response.json())  # returns json