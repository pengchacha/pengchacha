#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'livvy'

import tornado.web


class HomeHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        return self.render("home/index.html")
