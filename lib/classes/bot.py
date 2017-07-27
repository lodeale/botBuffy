#!/usr/bin/env python
# -*- coding: utf-8 -*

class Bot(object):
	_data = {}
	__connect=''
	__auth=''
	__error=''

	def setData(self,data):
		self._data = data

	def setConnect(self,connect):
		self.__connect = connect

	def getConnect(self):
		return self.__connect

	def setAuth(self,auth):
		self.__auth = auth

	def getAuth(self):
		return self.__auth

	def setError(self,txt):
		self.__error += "\n" + '-'*100 + "\n" + txt

	def getError(self):
		return self.__error