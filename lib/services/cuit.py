#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.src.servicesInterface import ServicesInterface
from lxml import html
import requests

class Cuit(ServicesInterface):
	_args=[]
	_host=['http://www.cuitonline.com/search.php']
	_query = ['q=']
	_pageText = ''
	_response = ''
	
	def execute(self):
		page = requests.get(self._host[0] + '?' + self._query[0] + self._args[0])
		self._pageText = html.fromstring(page.text)

	def getResult(self):
		if self.getName() and self.getCuit():
			return self._response

		return 'No se ha conseguido coincidencias... :('

	def getName(self):
		try:
			names = self._pageText.xpath('//span[@class="denominacion"]/text()')
			if len(names) == 1:
				self._response += 'Nombre : ' + str(names[0])
			elif len(names) > 1:
				self._response += "Los nombres son: "
				for i in names:
					self._response += i +", "
			else:
				return False

			return True
		except e:
			print "Error GetName: ", e

	def getCuit(self):
		cuit = self._pageText.xpath('//span[@class="cuit"]/text()')
		if len(cuit) == 1:
			self._response += ' Cuit : ' + str(cuit[0])
		elif len(cuit) > 1:
			self._response += " los cuits son: "
			for i in cuit:
				self._response += i +", "
		else:
			return False

		return True