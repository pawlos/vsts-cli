#cmd_req_coverage.py
from printers import header, bold, print_prerequisites

def help_req_coverage(self):
	print(header('Check coverage of formal requirements with test-runs'))
	print(bold('Requirements:'))
	print_prerequisites(prerequisites(self))

def prerequisites(vsts, args = None):
	return [vsts.status_token(),
			vsts.status_team_instance(),
			vsts.status_project_name()]

def do_req_coverage(self, args):
	pass