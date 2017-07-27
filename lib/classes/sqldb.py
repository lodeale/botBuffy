#!/usr/bin/env python
# -*- coding: utf-8 -*
import sqlobject

class Sqldb:
	__credential = {'user':'root','pass':'','host':'localhost','dbname':''}
	__connect = None
	
	def setData(self,data):
		self.__credential['user'] = data['user']
		self.__credential['pass'] = data['pass']
		self.__credential['host'] = data['host']
		self.__credential['dbname'] = data['dbname']

	def connect(self):
		try:
			print "\n[+]Conectando db por sqlobject...\n";
			handler = "mysql://%s:%s@%s/%s" % (self.__credential['user'],self.__credential['pass'],self.__credential['host'],self.__credential['dbname'])
			self.__connect = sqlobject.connectionForURI(handler)
			sqlobject.sqlhub.processConnection = self.__connect
		except Exception, e:
			print "Error Controlado: ",e


