import requests

django_endpoint = 'http://localhost:8000/api/school/1/update/'

# sending data from client

data = {'name': 'univerisity of Ibadan','location': 'Ibadan', 'founded': '1970'}
sending_request = requests.put(django_endpoint, json=data)  # return as python dict
print(sending_request.json())
