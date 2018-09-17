#cmd_list_test_runs.py

from printers import header, bold, print_statuses, print_prerequisites, _status

def help_list_test_runs(self):
	print(header('Lists all tests runs'))
	print(bold('Requires:'))
	print_prerequisites(prerequisites(self))

def prerequisites(vsts):
	return [vsts.status_token(),
			vsts.status_team_instance(),
			vsts.status_project_name()]


def do_list_test_runs(self, args):
	if not print_statuses(prerequisites(self)):
		return

	result = self.vsts_request.get(self.project_name, '_apis/test/runs?planId={}&includeRunDetails=true&api-version=5.0-preview.2'.format(self.test_plan))
	if not result:
		return
	
	_print_test_runs(result)


def _print_test_runs(test_runs):
	print(header('Test runs:'))
	for t in test_runs['value']:
		print('Id: {}, Name: {}, Status: {}'.format(
				bold(t['id']), bold(t['name']), _status(t['state'])
			))