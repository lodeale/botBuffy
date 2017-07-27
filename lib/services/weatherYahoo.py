#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.src.servicesInterface import ServicesInterface
import urllib2,json

class WeatherYahoo(ServicesInterface):
	_args=['none']
	_responseJson = ''
	_response = ''
	_query = ['https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22','argumentos','%2C%20Ar%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys']

	def __init__(self):
		super(WeatherYahoo, self).__init__()

	def execute(self):
		self._query[1] = self._args[0].capitalize()
		request = urllib2.Request(''.join(self._query))
		response = urllib2.urlopen(request)
		responseJson = response.read()
		self._responseJson = json.loads(responseJson)
		self.getResponse()
	
	def getResponse(self):
		if self._responseJson['query']['results'] != None:
			self._response = "En " + self._responseJson['query']['results']['channel']['location']['city'] + " " + self._responseJson['query']['results']['channel']['location']['country']
			self._response += " los datos del tiempo son: "
			self._response += "Humedad(" + self._responseJson['query']['results']['channel']['atmosphere']['humidity'] + ")"
			self._response += " Temperatura(" + self._responseJson['query']['results']['channel']['item']['condition']['temp'] + ")"
			self._response += " Tiempo(" + self._responseJson['query']['results']['channel']['item']['forecast'][0]['date'] + " - " + self._responseJson['query']['results']['channel']['item']['forecast'][0]['text'] + ")"
		else:
			self._response = 'No se encontro la provincia o ciudad'

	def getResult(self):
		return self._response
