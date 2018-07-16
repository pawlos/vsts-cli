#cmd_test_plan.py
from printers import error, ok, bold, header


def status_test_plan(self):
	return bold('Test plan: ') + (error('not set') if self.test_plan is None else ok(self.test_plan))

def help_test_plan(self):
	print(header('Set test plan id'))
	print(self.status_test_plan())

def do_test_plan(self, args):
	if args == '':
		print(error('Test plan id not set'))
		return

	self.test_plan = args
	print(self.status_test_plan())