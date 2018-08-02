#cmd_list_queries.py
from printers import error, bold, header, print_prerequisites, print_statuses
import pprint

def help_list_queries(self):
	print(header('Returns the list of all queries that user has access to'))
	print(bold('Requires:'))
	print_prerequisites(prerequisites(self))

def prerequisites(vsts):
	return [vsts.status_token(),
			vsts.status_team_instance(),
			vsts.status_project_name()]

def do_list_queries(self, args):
	if not print_statuses(prerequisites(self)):
		return
		
	result = self.vsts_request.get(self.project_name, '_apis/wit/queries?$expand=all&$depth=1&api-version=5.0-preview.2')
	
	_print_list_queries(result)

def _print_list_queries(queries):
	print(header('Queries:'))
	for q in queries['value']:
		print('Id: {}, Name: {}'.format(bold(q['id']), bold(q['name'])))
		children = q['children']
		if children is not None:
			for c in children:
				print('\tId: {}, Name: {}'.format(bold(c['id']),bold(c['name'])))