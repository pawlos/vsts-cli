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

def print_suites(d):
	print(header('Test suites:'))
	for s in d:
		print('Id: {}, Name: {}'.format(bold(s.id), bold(s.name)))

def print_projects(projects):
	print(header('Projects:'))
	for p in projects:
		print_project(p)

def print_project(project):
	print('Id: {}, Name: {}'.format(bold(project.id), bold(project.name)))

def print_tests_plans(plans):
	print(header('Test plans:'))
	for p in plans:
		print('Id: {}, Name: {}'.format(bold(p.id), bold(p.name)))

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

def print_test_cases(test_cases):
	for t in test_cases['value']:
		print(t)
		print('Id: {}, Tester: {}'.format(
			bold(t['testCase']['id']), bold(t['pointAssignments'][0]['tester']['displayName'])
		))

def _status(status):
	if status == 'InProgress' or status == 'NeedsInvestigation':
		return inconclusive(status)
	if status == 'Completed':
		return ok(status)
	return bold(status)

def print_test_runs(test_runs):
	print(header('Test runs:'))
	for t in test_runs['value']:
		print('Id: {}, Name: {}, Status: {}'.format(
				bold(t['id']), bold(t['name']), _status(t['state'])
			))
