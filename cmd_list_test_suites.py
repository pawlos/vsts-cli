#cmd_list_test_suites.py
from printers import bold, header, print_prerequisites, print_statuses
from models import TestSuite

def help_list_test_suites(self):
	print(header('Lists tests suites'))
	print(bold('Requires:'))
	print_prerequisites(prerequisites(self))

def prerequisites(vsts):
	return [vsts.status_token(),
			vsts.status_team_instance(),
			vsts.status_project_name(),
			vsts.status_test_plan()]

def do_list_test_suites(self, args):
	if not print_statuses(prerequisites(self)):
		return

	if self.vsts_test_suites is None or self.force:
		result = self.vsts_request.get(self.project_name, '_apis/test/plans/{}/suites?api-version=5.0-preview.2'.format(self.test_plan))
		self.vsts_test_suites = [
			TestSuite(d) for d in result['value']
		]

	_print_suites(self.vsts_test_suites)

def _print_suites(d):
	print(header('Test suites:'))
	for s in d:
		print('Id: {}, Name: {}'.format(bold(s.id), bold(s.name)))