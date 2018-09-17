#cmd_list_queries.py
from printers import bold, header, print_prerequisites, print_statuses, indent
from models import Query

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
	
	if self.queries is None or self.force:
		result = self.vsts_request.get(self.project_name, '_apis/wit/queries?$expand=all&$depth=1&api-version=5.0-preview.2')
		self.queries = [Query(v) for v in result['value']]
	_print_list_queries(self.queries)

def _print_list_queries(queries):
	print(header('Queries:'))
	for q in queries:
		print('Id: {}, Name: {}'.format(bold(q.id), bold(q.name)))
		if q.children is not None:
			for c in q.children:
				print(indent('Id: {}, Name: {}'.format(bold(c.id),bold(c.name))))
