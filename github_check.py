import requests
from pprint import pprint
import json
import os

# response = requests.get('https://api.github.com/zen')
# pprint('Response received: %s'%(response.text))


def fetch_user_details(user_info):
	pprint("Username: %s"%(user_info['login']))
	pprint("Name: %s"%(user_info['name']))
	pprint("Followers: %s"%(user_info['followers']))
	pprint("Following: %s"%(user_info['following']))
	pprint("Repos url: %s"%(user_info['repos_url']))


def getting_headers(username):
	response = os.system('curl -i https://api.github.com/users/{}'.format(username))
	return response

def authenticate_github_user(username):
	response = os.system('curl -i -u {} https://api.github.com/users/{}'.format(username, username))
	return response

# fetching user details:
username = raw_input('Please enter your github username: ')
response = requests.get('https://api.github.com/users/{}'.format(username), headers={"Content-Type": "application/json"})
user_info = json.loads(response.text)
fetch_user_details(user_info)

value = input('To fetch headers as well press 1 \n To authenticate user press 2 \n')

# import ipdb; ipdb.set_trace()

if value == 1:
	response = getting_headers(username)
	pprint(response)
else:
	response = authenticate_github_user(username)
	print(response)
