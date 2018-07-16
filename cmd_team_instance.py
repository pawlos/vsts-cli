#cmd_team_instance.py
from printers import error, ok, bold, header

def status_team_instance(self):
	return bold('Team instance: ') + (error('Not set') if self.team_instance is None else ok(self.team_instance))

def help_team_instance(self):
	print(header('Sets the team instance for the VSTS reuqests.\n')+
		self.status_team_instance()
	)

def do_team_instance(self, args):
	'''Sets the team instance for the VSTS requests'''
	if args == '':
		print(error('Team instance not provided'))
		return

	self.team_instance = 'https://{}.visualstudio.com'.format(args)
	print(self.status_team_instance())
	self.setup_connection()