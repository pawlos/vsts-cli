#vsts-query.py
import cmd

from vsts.vss_connection import VssConnection

from printers import *
from models import *
from vsts_request import *

class VSTSQuery(cmd.Cmd):
	from cmd_token import do_token, help_token, status_token
	from cmd_team_instance import do_team_instance, help_team_instance, status_team_instance
	from cmd_project_name import do_project_name, help_project_name, status_project_name
	from cmd_list_projects import do_list_projects, help_list_projects
	from cmd_list_test_plans import do_list_test_plans, help_list_test_plans
	from cmd_list_test_suites import do_list_test_suites, help_list_test_suites
	from cmd_test_plan import do_test_plan, help_test_plan, status_test_plan
	from cmd_test_suite import do_test_suite, help_test_suite, status_test_suite
	from cmd_project_details import do_project_details, help_project_details
	from cmd_list_test_runs import do_list_test_runs, help_list_test_runs
	from cmd_list_test_cases import do_list_test_cases, help_list_test_cases
	from cmd_list_queries import do_list_queries, help_list_queries
	
	def __init__(self):
		super(VSTSQuery, self).__init__()
		self.intro = header('VSTS CLI @ Paweł Łukasik 2018')
		self.prompt = bold('(VSTS)> ')
		self.team_instance = None
		self.token = None
		self.credentials = None
		self.connection = None
		self.core_client = None
		self.vsts_projects = None
		self.vsts_test_plans = None
		self.vsts_request = None
		self.project_name = None
		self.vsts_test_suites = None
		self.test_plan = None
		self.test_suite = None

	def setup_connection(self):
		if self.team_instance != None and self.credentials != None:
			self.connection = VssConnection(base_url=self.team_instance, 
										creds=self.credentials)
			self.core_client = self.connection.get_client('vsts.core.v4_0.core_client.CoreClient')
			self.vsts_request = VSTSRequest(self.team_instance, self.token)
			print(ok('Connection to VSTS established'))

	def help_exit(self):
		print(header('Exits the tool'))

	def do_exit(self, args):
		print(bold('Thank you for using VSTS CLI.'))
		print(ok('Bye')+', '+ok('bye!'))
		return True