#cmd_team_instance.py
from printers import error, ok, bold, header, print_prerequisites

def status_team_instance(self):
	return (self.team_instance is None, 
			bold('Team instance: ') + (error('Not set') if self.team_instance is None else ok(self.team_instance)))

def help_team_instance(self):
	print(header('Sets the team instance for the VSTS reuqests.'))
	print_prerequisites(prerequisites(self))

def prerequisites(vsts):
	return [vsts.status_team_instance()]

def do_team_instance(self, args):
	if args == '':
		print(error('Team instance not provided'))
		return

	self.team_instance = 'https://{}.visualstudio.com'.format(args.lstrip('='))
	print_prerequisites(prerequisites(self))
	self.setup_connection()