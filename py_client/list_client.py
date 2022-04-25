import requests
from getpass import getpass




auth_endpoint = 'http://localhost:8000/api/auth/'

username = input("What is your username?\n")
password = getpass("What is your password\n")
# getting token for authentication


data = {'username':username, 'password':password}
response = requests.post(auth_endpoint, json=data)  


if response.status_code == 200:
	token = response.json()['token']
	# headers = {
	# 'Authorization': f"Token {token}"
	# }

	# using Bearer
	headers = {
	'Authorization': f"Bearer {token}"
	}
	django_endpoint = 'http://localhost:8000/api/school/'

	# sending data from client

	response = requests.get(django_endpoint, headers=headers)  
	print(response.text)
	print(type(response.text))
	print(response.json())
	print(type(response.json()))


print("End of the session")