#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'livvy'


import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
