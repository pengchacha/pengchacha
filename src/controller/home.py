#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'livvy'

import base
import logging


class HomeHandler(base.BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        logging.getLogger("site").info("home page")
        return self.render("home/index.html")
