#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'livvy'

import tornado.web
import tornado.options
import tornado.options
import tornado.httpserver
import tornado.ioloop
import torndb
import os.path
import controller.home
import logging
import loggingConfig

tornado.options.define("port", default=8888, help="run the given port",
                       type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", controller.home.HomeHandler),

        ]
        settings = dict(
            site_title=u"PengChaCha",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookie=True,
            cookie_secret="傻羊ASFfgshhajHJkwiqksmsKKd_asjjksaLsesdl",
            login_url="/account/login",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = torndb.Connection(host='localhost', database='pengchacha',
                                    user="root", password='livvy')


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    logging.getLogger("site").info("start")
    main()

