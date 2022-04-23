import requests

django_endpoint = 'http://localhost:8000/api/school/4/delete/'

deleting_request = requests.delete(django_endpoint)
print(deleting_request.status_code)