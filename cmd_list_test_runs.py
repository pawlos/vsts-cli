#cmd_list_test_runs.py

from printers import header, bold, error, print_test_runs

def help_list_test_runs(self):
	print(header('Lists all tests runs'))
	print(bold('Requires:'))
	print(self.status_token())
	print(self.status_team_instance())
	print(self.status_project_name())

def do_list_test_runs(self, args):
	if self.project_name is None:
		print(error('Project name not set'))
		return
	if self.vsts_request is None:
		print(error('Connection to VSTS not established'))
		return

	print_test_runs(
		self.vsts_request.get(self.project_name, '_apis/test/runs?api-version=5.0-preview.2'))
