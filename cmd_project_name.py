#cmd_project_name.py
from printers import error, ok, bold, header

def status_project_name(self):
	return bold("Project name: ")+ (error('not set') if self.project_name is None else ok(self.project_name))

def help_project_name(self):
	print(header('Sets the project name for future requests'))
	print(self.status_project_name())

def do_project_name(self, args):
	if args == '':
		print(error('Project name not provided'))
		return

	self.project_name = args
	print(self.status_project_name())