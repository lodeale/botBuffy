import httplib
from urllib import quote_plus
from lib.services.cuit import Cuit
from lib.services.weatherYahoo import WeatherYahoo
from lib.models.web_services import Web_services
from lib.models.users import Users
import json

class Script(object):
	_services = {}
	_servicesApi = {}
	_dbinstance = None

	""" Guarda todo los servicios disponible en la base de datos """
	def setServices(self):
		if self._servicesApi == {}:
			self._servicesApi = Web_services.select()

	def findServicesForWord(self,word):
		print "def: findServicesForWord", self._servicesApi
		match = 0
		serviceMatch = []
		for s in self._servicesApi:
			print "Endpoing: ",s.endpoint, " Keyword: " , s.keywords
			for w in word.split(' '):
				if str(s.keywords).find(w) != -1: match += 1#keywords
				if str(s.keywords).find('everthingKeyword') != -1: match += 1 #everthing keywords
			if match > 0: serviceMatch.append(s.endpoint)#endpoint
			match = 0
		print "findServicesForWord return: ",serviceMatch
		return serviceMatch

	""" - @args= get tiene que devolver un string con toda la ruta completa.
		- El endpoint es la url del servicio.
		- Esta funcion solo hace un get a sentence
		- @return retorna la respeusta del servicio"""
	def getServices(self,endpoint,get):
                try:
                    connection = httplib.HTTPConnection(endpoint)
                    print "GET: ",endpoint,"/sentence" + quote_plus(get)
                    connection.request("GET","/sentence" + quote_plus(get) )
                    result = connection.getresponse()
                    print "[+]Resultado new ",result.status
                    if result.status == 200:
                            data = result.read()
                            print "[+]Resultado new ",data
                            return self.decodeMessage(data)
                    else:
                            print "[-] Error response", result.status
                            return False
                except:
                    print "Exception error getServices"

		connection.close()

	def putServices(self,endpoint,data,idUser):
		data_json = json.dumps({'message': data,'user_id':idUser})
		headers = {"Content-type":"application/json"}
		connection = httplib.HTTPConnection(endpoint)
		print "PUT: ",endpoint," ",get
		connection.request("PUT","/sentence/",data_json,headers=headers)
		result = connection.getresponse()
		if response.status == "OK":
			print "Response PUT: OK"
		else:
			print "Error :", response.status, " - ", response.reason
		connection.close()

	def decodeMessage(self,data):
		result = json.loads(data)
		resultMsg = result['msg']
		for idu in result['users_ids']:
			try:
				userReplace = Users.selectBy(id=idu)[0]
			except:
				print "[?] Error en el pedido de usuario segun el id: %s" % idu
				userReplace = Users.selectBy(user='Anonymous@anonymous')[0]
				print "User: ",userReplace
			resultMsg = resultMsg.replace("%us_id",userReplace.user,1)

		print "Return decodeMessage: " ,resultMsg
		return resultMsg


