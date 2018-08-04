#cmd_test_plan.py
from printers import error, ok, bold, header, print_prerequisites


def status_test_plan(self):
	return (self.test_plan is None, 
			bold('Test plan: ') + (error('not set') if self.test_plan is None else ok(self.test_plan)))

def complete_test_plan(self, text, line, begidx, endidx):
	return [str(p.id) for p in self.vsts_test_plans if str(p.id).startswith(text)]

def help_test_plan(self):
	print(header('Set test plan id'))
	print_prerequisites(prerequisite(self))

def prerequisite(vsts):
	return [vsts.status_test_plan()]

def do_test_plan(self, args):
	if args == '':
		print(error('Test plan id not set'))
		return

	self.test_plan = args
	print_prerequisites(prerequisite(self))