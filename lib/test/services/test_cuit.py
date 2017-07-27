import unittest2 as unittest
from lib.services.cuit import Cuit

class testCuit(unittest.TestCase):
	_obj = ''

	def setUp(self):
		self._obj = Cuit()
		self._obj._args = ['31720792']
		self._obj.execute()

	def test_getName(self):
		self.assertTrue(self._obj.getName())

	def test_getCuit(self):
		self.assertTrue(self._obj.getCuit())

if __name__ == '__main__':
	unittest.main()