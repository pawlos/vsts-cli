#cmd_list_projects.py
from printers import bold, header, print_prerequisites, print_statuses
from models import Project

def help_list_projects(self):
	print(header('Lists projects in the team instance'))
	print(bold('Requires: '))
	print_prerequisites(prerequisites(self))

def prerequisites(vsts):
	return [vsts.status_token(),
			vsts.status_team_instance()]

def do_list_projects(self, args):
	if not print_statuses(prerequisites(self)):
		return

	if self.vsts_projects is None or self.force:
	   self.vsts_projects = [Project(p.id, p.name) for p in 
						  	 self.core_client.get_projects()]
	
	_print_projects(self.vsts_projects)


def _print_projects(projects):
	print(header('Projects:'))
	for p in projects:
		_print_project(p)

def _print_project(project):
	print('Id: {}, Name: {}'.format(bold(project.id), bold(project.name)))
