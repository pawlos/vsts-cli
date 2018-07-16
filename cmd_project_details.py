#cmd_project_details.py
from printers import error, bold, header, print_project
import uuid

def help_project_details(self):
	print(header('Get details of the selected project'))
	print(bold('Requires:'))
	print(self.status_token())
	print(self.status_team_instance())
	print('id of the project passed as an argument')

def do_project_details(self, args):
	if args == '':
		print(error('Project id not passed as an argument'))
		return

	project = self.core_client.get_project(uuid.UUID(args))
	print_project(project)