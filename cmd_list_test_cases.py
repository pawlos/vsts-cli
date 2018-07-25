#cmd_list_test_case.py
from printers import header, bold


def help_list_test_cases(self):
	print(header('List all the test cases from test suite in a test plan'))
	print(bold('Requires'))
	print(self.status_token())
	print(self.status_team_instance())
	print(self.status_project_name())
	print(self.status_test_plan())
	print(self.status_test_suite())

def do_list_test_cases(self, args):
	if self.test_plan is None:
		print(self.status_test_plan())
		return
	if self.test_suite is None:
		print(self.status_test_suite())
		return

	_print_test_cases(
		self.vsts_request.get(
			self.project_name,
			'_apis/test/plans/{}/suites/{}/testcases?api-version=5.0-preview.2'.format(self.test_plan, self.test_suite)),
		)

def _print_test_cases(test_cases):
	for t in test_cases['value']:
		print(t)
		print('Id: {}, Tester: {}'.format(
			bold(t['testCase']['id']), bold(t['pointAssignments'][0]['tester']['displayName'])
		))