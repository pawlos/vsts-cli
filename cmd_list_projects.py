#cmd_list_projects.py
from printers import error, bold, header, print_projects
from models import Project

def help_list_projects(self):
	print(header('Lists projects in the team instance'))
	print(bold('Requires: '))
	print(self.status_token())
	print(self.status_team_instance())

def do_list_projects(self, args):
	if self.core_client is None:
		print(error('Connection to VSTS not established'))
		return

	if self.vsts_projects is None or self.force:
	   self.vsts_projects = [Project(p.id, p.name) for p in 
						  	 self.core_client.get_projects()]
	
	print_projects(self.vsts_projects)