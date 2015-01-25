#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'zy'

import tornado.web
import base

#ask for a tutorial
class AskHandler(base.BaseHandler):
    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        #user_id = self.get_secure_cookie("pengchacha-user")
        user_id = 1 #for test
        if not user_id:
            self.redirect("/account/login")
            return
        quest_title = self.get_argument("quest_title",None)
        print quest_title
        quest_content = self.get_argument("quest_content",None)
        print quest_content

        print user_id
        #need to add try catch block
        quest = self.db.execute("insert into question (user_id,question,description) values (%s,%s,%s)",user_id,quest_title,quest_content)
        self.finish()
        return

