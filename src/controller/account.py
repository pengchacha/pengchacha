#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'livvy'

import base


class LoginHandler(base.BaseHandler):
    def get(self, *args, **kwargs):
        return self.render("account/login.html")