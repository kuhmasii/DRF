import requests

django_endpoint = 'http://localhost:8000/api/school/'

# sending data from client

response = requests.get(django_endpoint)  
print(response.text)
