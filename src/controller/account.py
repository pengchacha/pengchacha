#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'livvy'

import base

__all__ = ['LoginHandler', 'RegisterHandler']


class LoginHandler(base.BaseHandler):
    def get(self, *args, **kwargs):
        return self.render("account/login.html")


class RegisterHandler(base.BaseHandler):
    def post(self, *args, **kwargs):
        name = self.get_argument("name")
        email = self.get_argument("email")



