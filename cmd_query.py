#cmd_query.py
from printers import error, bold, header, ok, indent, print_prerequisites, print_statuses
from models import WorkItemRelation, WorkItem
import pprint

def help_query(self):
	print(header('Runs selected query'))
	print(bold('Requirements:'))
	print_prerequisites(prerequisites(self))

def complete_query(self, text, line, begidx, endidx):
	return _get_query_ids(self.queries, text)

def _get_query_ids(queries, text):
	ids = []
	if queries is None:
		return []
	for q in queries:
		if q.children is not None:
			ids += _get_query_ids(q.children, text)
		if str(q.id).startswith(text):
			ids.append(str(q.id))
	return ids

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

	columns = result['columns']
	if 'workItemRelations' in result:
		relations = result['workItemRelations']
		relations = list(map(lambda wir: WorkItemRelation(wir), relations))

		for wir in relations:
			if wir.source is not None and wir.source.details is None:
				wir.source.details = self.vsts_request.getAbsolute(wir.source.url)
			if wir.target is not None and wir.target.details is None:
				wir.target.details = self.vsts_request.getAbsolute(wir.target.url)

		_print_query(relations, args, columns)
	elif 'workItems' in result:
		workItems = result['workItems']
		items = list(map(lambda wi: WorkItem(wi), workItems))

		for wi in items:
			wi.details = self.vsts_request.getAbsolute(wi.url)

		_print_query(items, args, columns)

def _print_query(result, id, columns):
	print(header('Query ')+bold(id)+header(' results'))
	print(header("Columns: ")+', '.join(map(lambda c: c['name'], columns)))
	print(header('Work items in the query:'))

	for i in result:
		print(i)
