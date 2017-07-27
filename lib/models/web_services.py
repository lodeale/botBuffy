#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlobject

class Web_services(sqlobject.SQLObject):
	endpoint = sqlobject.StringCol(length=250)
	name = sqlobject.StringCol(length=30)
	keywords = sqlobject.StringCol()
	datekeyword = sqlobject.DateCol()