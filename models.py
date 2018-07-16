#models for VSTS

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
	def __init(self, data):
		self.id = int(data('id'))