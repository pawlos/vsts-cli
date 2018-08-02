#cmd_list_test_plans.py
from printers import error, bold, header, print_prerequisites, print_statuses
from models import TestPlan

def help_list_test_plans(self):
	print(header('Returns list of tests plans for the selected project'))
	print(bold('Requires:'))
	print_prerequisites(prerequisites(self))

def prerequisites(vsts):
	return [vsts.status_token(),
			vsts.status_team_instance(),
			vsts.status_project_name()]

def do_list_test_plans(self, args):
	if not print_statuses(prerequisites(self)):
		return

	if self.vsts_test_plans is None or self.force:
		result = self.vsts_request.get(self.project_name, '_apis/test/plans?filterActivePlans=true&api-version=5.0-preview.2')
		vsts_test_plans = [
			TestPlan(d) for d in 
			result['value']
		]

	_print_tests_plans(vsts_test_plans)

def _print_tests_plans(plans):
	print(header('Test plans:'))
	for p in plans:
		print('Id: {}, Name: {}'.format(bold(p.id), bold(p.name)))