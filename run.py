# !/usr/bin/evn python
# -*-  coding:utf-8 -*-

__auther__ = 'sennado'

import sys  
if sys.prefix[-2:] is not '35':
    print(sys.prefix[-2:] == '35') 

from tornado import web, ioloop, gen, options

from config import *

 

print(mysqlDb)
