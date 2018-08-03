#cmd_query.py
from printers import error, bold, header, ok, indent, print_prerequisites, print_statuses
from models import WorkItemRelation, WorkItem
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
	if not result:
		return

	_print_query(result, args)

def _print_query(result, id):
	print(header('Query ')+bold(id)+header(' results'))
	print(header("Columns: ")+', '.join(map(lambda c: c['name'],result['columns'])))
	print(header('Work items in the query:'))
	if 'workItemRelations' in result:
		relations = result['workItemRelations']
		relations = map(lambda wir: WorkItemRelation(wir), relations)
		print('\n'.join([str(wir) for wir in relations]))
	elif 'workItems' in result:
		workItems = result['workItems']
		workItems = map(lambda wi: WorkItem(wi), workItems)
		print('\n'.join([str(wi) for wi in workItems]))
