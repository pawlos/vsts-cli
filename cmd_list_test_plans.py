#cmd_list_test_plans.py
from printers import error, bold, header, print_tests_plans
from models import TestPlan

def help_list_test_plans(self):
	print(header('Returns list of tests plans for the selected project'))
	print(bold('Requires:'))
	print(self.status_token())
	print(self.status_team_instance())
	print(self.status_project_name())

def do_list_test_plans(self, args):
	if self.vsts_request == None or self.project_name == None:
		print(error('Cannot run command. Connection or project_name not set'))
		return

	if self.vsts_test_plans is None or self.force:
		result = self.vsts_request.get(self.project_name, '_apis/test/plans?filterActivePlans=true&api-version=5.0-preview.2')
		vsts_test_plans = [
			TestPlan(d) for d in 
			result['value']
		]

	print_tests_plans(vsts_test_plans)