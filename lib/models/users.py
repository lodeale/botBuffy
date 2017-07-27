#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlobject

class Users(sqlobject.SQLObject):
	user = sqlobject.StringCol(length=250)