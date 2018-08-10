#models for VSTS
import uuid
from printers import bold

class Project(object):
	def __init__(self, id, name):
		self.id = id
		self.name = name

class TestPlan(object):
	def __init__(self, data):
		self.id = int(data['id'])
		self.name = data['name']

class TestSuite(object):
	def __init__(self, data):
		self.id = int(data['id'])
		self.name = data['name']
		self.testCaseCount = data['testCaseCount']

class TestCase(object):
	def __init__(self, data):
		self.id = int(data['testCase']['id'])
		self.url = data['testCase']['url']
		self.data = data

class Query(object):
	def __init__(self, data):
		self.id = uuid.UUID(data['id'])
		self.name = data['name']
		self.children = None
		if 'children' in data:
			children = data['children']
			self.children = [Query(d) for d in children]

class WorkItemRelation(object):
	def __init__(self, data):
		self.source = None if data['source'] is None else WorkItem(data['source'])
		self.target = None if data['target'] is None else WorkItem(data['target'])

	def __str__(self):
		return (('' if self.source is None else 'Source: '+str(self.source)+' → ')+
			    ('' if self.target is None else 'Target: '+str(self.target)))

class WorkItem(object):
	def __init__(self, data):
		self.id = data['id']
		self.url = data['url']
		self.details = None

	def __str__(self):
		data = ('Url: '+self.url) if self.details is None else 'Title: '+bold(self.details['fields']['System.Title'])
		return 'Id: '+bold(self.id)+', '+data
