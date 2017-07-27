#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xmpp
import re
import urllib
from email.Utils import parseaddr
from lib.script.script import Script
from lib.models.users import Users
import time

class Gtalk(Script):

	_site = 'talk.google.com'
	_port = 5223
	_domain = 'gmail.com'
	_instance = None
	_handler = None
	_message = None

	def __new__(self,*args,**kwargs):
		if not self._instance:
			self._instance = super(Gtalk, self).__new__(self,*args,**kwargs)

		return self._instance

	def connect(self):
		try:
			self._handler = xmpp.Client(self._domain)
			self._handler.connect(server=(self._site,self._port))
			return 1
		except (NameError, ValueError):
			print "Error de conexión"
			print str(NameError) + ': ' + str(ValueError)
			return 0

	def auth(self,user,email,name):
		try:
			self._handler.auth(user,email,name)
			self._handler.sendInitPresence()
			return 1
		except:
			print "No se pudo autentificar"
			return 0

	def makeMessage(self,to,msg):
		self._message = xmpp.Message(to, msg)
		self._message.setAttr('type', 'chat')

	def send(self):
		try:
			self._handler.send(self._message)
			return 1
		except(NameError,ValueError):
			print "Error: No se pudo enviar el mensaje"
			print str(NameError) + ': ' + str(ValueError)
			return 0

	def listening(self):
		self._handler.RegisterHandler('message', self.message_handler)
		self._handler.RegisterHandler('presence', self.presenceContact)
		while self._handler.Process(1):
			pass

	def presenceContact(self,con,event):
		self._handler.sendInitPresence(requestRoster=1)
		myroster = self._handler.getRoster()
		fromjid = event.getFrom().getStripped()
		status = myroster.getStatus(fromjid)
		hours = time.strftime("%H")
		if fromjid == 'lodeale@gmail.com' and  hours == '07':
			self._handler.send(xmpp.Message( fromjid , "Buen diaaaaa... exitos para hoy!!", typ='chat'))
		print "*"*50
		print "fecha", hours
		print "[----------------]\nmyrestore: ",myroster
		print "\nfromjid: ",fromjid,"\nstatus: ",status
		print "\ncoon: ",dir(con)
		print "\nevent: ",event.getStatus()
		print "\nhandler: ",self._handler.Roster.getRoster()
		print "*"*50

	def message_handler(self,connect_object, message_node):
		#message = "estoy en el Message_handler"
		#connect_object.send( xmpp.Message( message_node.getFrom() ,message))
		try:
			inputMsg = message_node.getBody()
			inputMsg = str(inputMsg).lower()
			#Imprimimos lo que viene del cliente
			print "*"*50
			#*****************************
			#Usuario
			#*****************************
			userEmail = str(message_node.getFrom())
			print "[+]UserEmail ", userEmail,"\n"
			if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',userEmail):
				print "Email Valid"
				queryUser = Users.selectBy(user=userEmail)
				if queryUser.count() == 0:
					print "[+]Save User....\n"
					u = Users(user=userEmail)
					if u.id > 0 :
						print "[+]User Save OK!\n"
					else:
						print "[?]User No Save \n"
			else:
				userTmp = userEmail.split('/')
				print "UserExist2: " , userTmp
				if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',userTmp[0]):
					userEmail = userTmp[0]
					print "Email 2 Valid"
			#userOn contiene la clase Usuario activo
			userOn = Users.selectBy(user=userEmail)[0]
			print "[+]userOn: ",userOn
			print "[+]Id: ", userOn.id

			print type(inputMsg), inputMsg
			print "*"*50
			#*****************************
			#servicios
			#*****************************
			if inputMsg in ['None','none']:
				return False
			else:
				print "findServicesForWord"
				matchServices = self.findServicesForWord(inputMsg)
				for s in matchServices:
					print "Servicio [",s,"]"
					array_message = inputMsg.split(' ')
					result = self.getServices(s, '/'+str(userOn.id)+'/' + ' '.join(array_message))
					print '[+] Imprimiento endpoint y get: ',s, '/'+str(userOn.id)+'/' + ''.join(array_message)
					print "Resultado: ",result
					if result:
						connect_object.send(xmpp.Message( message_node.getFrom() , result, typ='chat'))
					else:
						print "Devolvio Falso"
		except Exception, e:
			print "Error %s " % e
