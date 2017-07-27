###
# Implementation Interface for any API
#
class ApiInterface(object):
	_name = ''
	_endpoint=[]
	_sentence=[]
	_keywords=[]
	
	def getKeywords(self):
		raise NotImplementedError()

	def setSentence(self):
		raise NotImplementedError()

	def execute(self):
		raise NotImplementedError()

	def getResult(self):
		raise NotImplementedError()