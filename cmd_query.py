#cmd_query.py
from printers import error, bold, header, indent
import pprint

def help_query(self):
	print(header('Runs selected query'))
	print(bold('Requirements:'))
	print(self.status_token())
	print(self.status_team_instance())
	print(self.status_project_name())
	print(bold('Query id - argument to the command'))


def do_query(self, args):
	if self.token is None:
		print(self.status_token())
		return
	if self.team_instance is None:
		print(self.status_team_instance())
		return
	if self.project_name is None:
		print(self.status_project_name())
		return

	if args == '':
		print(error('Missing query id'))
		return

	result = self.vsts_request.get(self.project_name, '_apis/wit/wiql/{}?api-version=5.0-preview.2'.format(args))

	_print_query(result, args)

def _print_query(result, id):
	print(header('Query ')+bold(id)+' results')
	print(header("Columns: ")+', '.join(map(lambda c: c['name'],result['columns'])))
	print(header('Work items in the query:'))
	relations = result['workItemRelations']
	print(indent(
		', '.join(map(lambda wi: str(wi['target']['id']), relations)))
	)
