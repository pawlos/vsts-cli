#vsts_request.py

from requests.auth import HTTPBasicAuth
import json
import requests
from printers import *
import sys

class VSTSRequest:

	def __init__(self, team_instance, token, debug = False):
		self.team_instance = team_instance
		self.token = token
		self.url = self.team_instance
		self.debug = debug

	def getAbsolute(self, url):
		if self.debug:
			print(url)
		resp = requests.get(url, auth=HTTPBasicAuth('', self.token))
		if resp.status_code != 200:
			return False
		return json.loads(resp.text)

	def get(self, project_name, query):
		if self.debug:
			print(self.url+'/'+project_name+'/'+query)
		print(bold('Request:'), end=' ')
		sys.stdout.flush()
		resp = requests.get(self.url+'/'+project_name+'/'+query, 
							auth=HTTPBasicAuth('',self.token))
		if resp.status_code != 200:
			print(error('failed.'))
			return False
		print(ok('successful.'))
		return json.loads(resp.text)