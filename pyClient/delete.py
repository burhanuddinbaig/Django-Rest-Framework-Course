import requests

product_id = input("What is the product Id you want to see?\n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not valid')

if product_id:
    endpoint = "http://localhost:8000/api/products/1/"

    get_response = requests.delete(endpoint)

    # print(get_response.text) # Print Raw Text Response
    print(get_response.status_code, get_response.status_code == 204)  # returns json