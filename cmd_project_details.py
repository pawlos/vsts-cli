#cmd_project_details.py
from printers import error, bold, header, ok, print_prerequisites, print_statuses
import uuid

def help_project_details(self):
	print(header('Get details of the selected project'))
	print(bold('Requires:'))
	print_prerequisites(prerequisites(self))

def project_name_status(args):
	project_name_not_set = args == '' or args is None
	return (project_name_not_set, 
		    bold('Project id: ') + (error('not passed as an argument') if project_name_not_set else ok(args)))

def prerequisites(vsts, args = None):
	return [(vsts.status_token()),
			(vsts.status_team_instance()),
			(vsts.status_project_name()),
			(project_name_status(args))]

def do_project_details(self, args):
	if not print_statuses(prerequisites(self)):
		return

	project = self.core_client.get_project(uuid.UUID(args))
	_print_project(project)

def _print_project(project):
	print('Id: {}, Name: {}'.format(bold(project.id), bold(project.name)))
