#cmd_test_suite.py
from printers import bold, error, ok, header, print_prerequisites

def status_test_suite(self):
	return (self.test_suite is None, 
		    bold('Test suite: ')+(error('not set') if self.test_suite is None else ok(self.test_suite)))

def help_test_suite(self):
	print(header('Selectes the test suite'))
	print_prerequisites(prerequisites(self))

def complete_test_suite(self, text, line, begidx, endidx):
	return [str(p.id) for p in self.vsts_test_suites if str(p.id).startswith(text)]

def prerequisites(vsts):
	return [vsts.status_test_suite()]

def do_test_suite(self, args):
	if args == '':
		print(error('Test suite not set'))
		return

	self.test_suite = args
	print_prerequisites(prerequisites(self))