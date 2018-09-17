from bcolors import *


def bold(s):
	return bcolors.BOLD+str(s)+bcolors.ENDC

def header(s):
	return bcolors.HEADER+str(s)+bcolors.ENDC

def ok(s):
	return bcolors.OKGREEN+str(s)+bcolors.ENDC

def info(s):
	return bcolors.WARNING+str(s)+bcolors.ENDC

def error(s):
	return bcolors.FAIL+str(s)+bcolors.ENDC

def inconclusive(s):
	return bcolors.WARNING+str(s)+bcolors.ENDC

def indent(s):
	return '\t'+str(s)

def print_statuses(statues):
	is_error = False
	for c, s in statues:
		if c:
			print(s)
			is_error = True
	return not is_error

def print_prerequisites(statuses):
	for c, s in statuses:
		print(s)

def _status(status):
	if status == 'InProgress' or status == 'NeedsInvestigation':
		return inconclusive(status)
	if status == 'Completed':
		return ok(status)
	return bold(status)
