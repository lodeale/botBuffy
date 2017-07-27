#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from config.credential import Credential
from lib.script.gtalk import Gtalk
from lib.script.telegram import Telegram
from lib.classes.sqldb import Sqldb
from lib.classes.bot import Bot


if __name__ == '__main__':
	try:
		#sqlobject
		sqlo = Sqldb()
		sqlo.setData(Credential._dbData)
		sqlo.connect()

		#Genero el bot
		c = Bot()
		c.setData(Credential._data)
                #c.setConnect(Gtalk())
		c.setConnect(Telegram())
		#Setting's services
		c.getConnect().setServices()
		#Connection to google talk or Telegram
		c.getConnect().connect()
		c.getConnect().auth(c._data['user'],c._data['passwd'],c._data['name'])

        #listening
		c.getConnect().listening()
	except Exception, e:
		print "Error en app.py: ", e


