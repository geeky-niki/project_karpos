import requests

endpoint = 'http://127.0.0.1:8000/cust/data'

get_response = requests.get(endpoint)
print(get_response.json())
print(type(get_response))