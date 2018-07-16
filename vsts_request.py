#vsts_request.py

from requests.auth import HTTPBasicAuth
import json
import requests
from printers import *
import sys

class VSTSRequest:

	def __init__(self, team_instance, token):
		self.team_instance = team_instance
		self.token = token
		self.url = self.team_instance


	def get(self, project_name, query):
		print(bold('Request:'), end=' ')
		sys.stdout.flush()
		resp = requests.get(self.url+'/'+project_name+'/'+query, 
							auth=HTTPBasicAuth('',self.token))
		if resp.status_code != 200:
			print(error('failed.'))
			return False
		print(ok('successful.'))
		return json.loads(resp.text)