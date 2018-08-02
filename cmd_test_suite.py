#cmd_test_suite.py
from printers import bold, error, ok, header, print_prerequisites

def status_test_suite(self):
	return (self.test_suite is None, 
		    bold('Test suite: ')+(error('not set') if self.test_suite is None else ok(self.test_suite)))

def help_test_suite(self):
	print(header('Selectes the test suite'))
	print_prerequisites(prerequisites(self))

def prerequisites(vsts):
	return [vsts.status_test_suite()]

def do_test_suite(self, args):
	if args == '':
		print(error('Test suite not set'))
		return

	self.test_suite = args
	print_prerequisites(prerequisites(self))