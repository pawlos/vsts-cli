#token.py
from printers import error, ok, bold, header
from msrest.authentication import BasicAuthentication

def status_token(self):
	return bold('Token: ') + (error('not set') if self.token is None else ok('************ (set)'))

def help_token(self):
	print(header('Sets the token for the VSTS requests.\n')+self.status_token())

def do_token(self, args):
	if args == '':
		print(error('Token not provided'))
		return

	self.token = args
	self.credentials = BasicAuthentication('', self.token)
	print(self.status_token())
	self.setup_connection()