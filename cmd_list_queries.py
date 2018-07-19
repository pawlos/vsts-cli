#cmd_list_queries.py
from printers import error, bold, header, print_list_queries
import pprint

def help_list_queries(self):
	print(header('Returns the list of all queries that user has access to'))
	print(bold('Requires:'))
	print(self.status_token())
	print(self.status_team_instance())
	print(self.status_project_name())

def do_list_queries(self, args):
	if self.project_name is None:
		print(self.status_project_name())
		return
	if self.token is None:
		print(self.status_token())
		return
	if self.team_instance is None:
		print(self.status_team_instance())
		return
		
	result = self.vsts_request.get(self.project_name, '_apis/wit/queries?$expand=all&$depth=1&api-version=5.0-preview.2')
	
	print_list_queries(result)
