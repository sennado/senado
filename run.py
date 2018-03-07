# !/usr/bin/evn python
# -*-  coding:utf-8 -*-

__auther__ = 'sennado'

import sys  

from tornado import web, ioloop, gen

from tornado.options import define, options
from config import *


define("port", default=8999, help="run port", type=int)

print(options.port)
print(mysqlDb)
settings = {
    'debug' : True
}

class MainHandler(web.RequestHandler):
    ''' docstring for MainHandler '''
    def get(self):
        
        self.write("Hello word!")

def main():
    return web.Application([
        (r"/", MainHandler),
    ], **settings)

if __name__ == "__main__":
    app = main()
    app.listen(options.port)
    ioloop.IOLoop.instance().start()   
