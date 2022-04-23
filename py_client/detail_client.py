import requests

print('Welcome to the Client side of the my App:)')
print("*" * 80)

# Moving to django
django_endpoint = 'http://localhost:8000/api/school/1/'

response = requests.get(django_endpoint)
print(response.text)
print(response.json())

# sending data from client
