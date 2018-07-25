from bcolors import *
import pprint


def bold(s):
	return bcolors.BOLD+str(s)+bcolors.ENDC

def header(s):
	return bcolors.HEADER+str(s)+bcolors.ENDC

def ok(s):
	return bcolors.OKGREEN+str(s)+bcolors.ENDC

def error(s):
	return bcolors.FAIL+str(s)+bcolors.ENDC

def inconclusive(s):
	return bcolors.WARNING+str(s)+bcolors.ENDC

def indent(s):
	return '\t'+str(s)

def print_tests_plan(plan):
	print(header('Test plan:'))
	print('Id: {}, Name: {}, Root suite id: {}'.format(
			bold(plan['id']), bold(plan['name']), bold(plan['rootSuite']['id'])
		))

def print_suite(suite):
	print(header('Test suite:'))
	print('Id: {}, Name: {}, Test cases count: {}'.format(
			bold(suite['id']), bold(suite['name']), bold(suite['testCaseCount'])
		))

def _status(status):
	if status == 'InProgress' or status == 'NeedsInvestigation':
		return inconclusive(status)
	if status == 'Completed':
		return ok(status)
	return bold(status)
