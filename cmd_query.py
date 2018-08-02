#cmd_query.py
from printers import error, bold, header, indent, print_prerequisites, print_statuses
import pprint

def help_query(self):
	print(header('Runs selected query'))
	print(bold('Requirements:'))
	print_prerequisites(prerequisites(self))

def status_query_id(args):
	query_not_set = args == '' or args is None
	return (query_not_set,
			header('Query id as argument: ')+(error('not provided') if query_not_set else ok(args)))

def prerequisites(vsts, args = None):
	return [
		vsts.status_token(),
		vsts.status_team_instance(),
		vsts.status_project_name(),
		status_query_id(args)
	]

def do_query(self, args):
	if not print_statuses(prerequisites(self, args)):
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
