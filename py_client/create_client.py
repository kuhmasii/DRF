import requests

django_endpoint = 'http://localhost:8000/api/school/'

# sending data from client

data = {'name': 'eksu', 'location': 'Ekiti', 'founded': '1950'}
sending_request = requests.post(django_endpoint, json=data)  # return as python dict
print(sending_request.json())
