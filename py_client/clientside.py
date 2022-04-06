import requests

print('Welcome to the Client side of the my App:)')
print("*" * 80)

endpoint = 'http://httpbin.org/'
endpoint = 'https://httpbin.org/anything'

get_response = requests.get(endpoint, data={'python':'Hello world'}) #the diffs is in the content_type
get_response = requests.get(endpoint, json={'python':'Hello world'})
print(get_response.text) returns a json file
print(get_response.json()) # turns it to python dict

# Moving to django
django_endpoint = 'http://localhost:8000/api/'

response = requests.get(django_endpoint)
print(response.text)
print(response.json())

# sending data from client

data = {'name':'UNIBEN', 'location':'BENIN', 'founded':'1950'}
sending_request = requests.post(django_endpoint, data={'name':'OAU'}) #return as a querydict object
sending_request = requests.post(django_endpoint, json=data) # return as python dict

print(sending_request.json())


get_response = requests.get(django_endpoint)
print(get_response.json())
