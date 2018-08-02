#cmd_list_test_case.py
from printers import header, bold, print_statuses, print_prerequisites


def help_list_test_cases(self):
	print(header('List all the test cases from test suite in a test plan'))
	print(bold('Requires:'))
	print_prerequisites(prerequisites(self))

def prerequisites(vsts):
	return [vsts.status_token(),
			vsts.status_team_instance(),
			vsts.status_project_name(),
			vsts.status_test_plan(),
			vsts.status_test_suite()]

def do_list_test_cases(self, args):
	if not print_statuses(prerequisites(self)):
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