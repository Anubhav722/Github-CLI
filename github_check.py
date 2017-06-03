import requests
from pprint import pprint
import json

response = requests.get('https://api.github.com/zen')
pprint('Response received: %s'%(response.text))

# fetching user details:
# import ipdb; ipdb.set_trace()
response = requests.get('https://api.github.com/users/Anubhav722', headers={"Content-Type": "application/json"})
user_info = json.loads(response.text)
# pprint("Blah")

pprint("Username: %s"%(user_info['login']))
pprint("Name: %s"%(user_info['name']))
pprint("Followers: %s"%(user_info['followers']))
pprint("Following: %s"%(user_info['following']))
pprint("Repos url: %s"%(user_info['resos_url']))