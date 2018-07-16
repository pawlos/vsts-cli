#cmd_test_suite.py
from printers import bold, error, ok

def status_test_suite(self):
	return bold('Test suite: ')+(error('not set') if self.test_suite is None else ok(self.test_suite))

def help_test_suite(self):
	print(header('Selectes the test suite'))
	print(self.status_test_suite())

def do_test_suite(self, args):
	if args == '':
		print(error('Test suite not set'))

	self.test_suite = args
	print(self.status_test_suite())
	'''vsts_print(
		vsts_request('_apis/test/plans/{}/suites/{}?$expand={}&api-version=5.0-preview.2'.format(test_plan_id, suite_id, expand)),
		print_suite)'''