#token.py
from printers import error, ok, bold, header, print_prerequisites
from msrest.authentication import BasicAuthentication

def status_token(self):
	return (self.token is None, 
		    bold('Token: ') + (error('not set') if self.token is None else ok('************ (set)')))

def help_token(self):
	print(header('Sets the token for the VSTS requests.'))
	print_prerequisites(prerequisites(self))

def prerequisites(vsts):
	return [vsts.status_token()]

def do_token(self, args):
	if args == '':
		print(error('Token not provided'))
		return

	self.token = args
	self.credentials = BasicAuthentication('', self.token)
	print_prerequisites(prerequisites(self))
	self.setup_connection()