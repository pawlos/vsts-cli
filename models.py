#models for VSTS
import uuid

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
		self.id = int(data['id'])

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
		return (('' if self.source is None else 'Source: '+str(self.source.id)+' → ')+
			    ('' if self.target is None else 'Target: '+str(self.target.id)))

class WorkItem(object):
	def __init__(self, data):
		self.id = data['id']
		self.url = data['url']
		self.details = None

	def __str__(self):
		return 'Id: '+str(self.id)+' Url: '+self.url