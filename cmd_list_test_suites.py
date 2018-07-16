#cmd_list_test_suites.py
from printers import error, bold, header, print_suites
from models import TestSuite

def help_list_test_suites(self):
	print(header('Lists tests suites'))
	print(bold('Requires:'))
	print(self.status_token())
	print(self.status_team_instance())
	print(self.status_project_name())
	print(self.status_test_plan())

def do_list_test_suites(self, args):
	if (self.vsts_request == None or 
		self.project_name == None):
		print(error('Cannot run command. Make sure connection to VSTS is establish.'))
		return

	if self.vsts_test_suites is None or self.force:
		result = self.vsts_request.get(self.project_name, '_apis/test/plans/{}/suites?api-version=5.0-preview.2'.format(self.test_plan))
		vsts_test_suites = [
			TestSuite(d) for d in result['value']
		]

	print_suites(vsts_test_suites)