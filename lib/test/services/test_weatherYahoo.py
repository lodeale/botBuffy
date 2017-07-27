import unittest2 as unittest
from lib.services.weatherYahoo import WeatherYahoo

class testWeatherYahoo(unittest.TestCase):
	_obj = ''

	def setUp(self):
		self._obj = WeatherYahoo()

	def test_responseJson_true(self):
		self._obj._args = ['resistencia']
		self._obj.execute()
		self.assertNotEqual(self._obj._responseJson['query']['results'], None)

	def test_responseJson_false(self):
		self._obj._args = ['alkj234osf']
		self._obj.execute()
		self.assertEqual(self._obj._responseJson['query']['results'], None)

if __name__ == '__main__':
	unittest.main()