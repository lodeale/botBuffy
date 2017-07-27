###
# Implementation Interface for any services
#
class ServicesInterface(object):
	_args=[]
	
	def execute(self):
		raise NotImplementedError()

	def getResult(self):
		raise NotImplementedError()