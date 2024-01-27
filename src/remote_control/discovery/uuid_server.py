from generate_uuid import get_uuid
"""from jinja2 import Template

import os
if not os.path.exists("index.http"):
    with open("template.j2","r") as f:
        template = f.read()

    tmp = Template(template)
    tmp = tmp.render({"content": get_uuid()})

    with open("index.http","w+") as f:
        f.write(tmp)

cmd = "bash uuid_server.sh"
os.system(cmd)"""
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(get_uuid())

    def make_app():
        return tornado.web.Application([ (r"/", MainHandler), ])  # URL Mapping

if __name__ == "__main__":
    app = MainHandler.make_app()
    app.listen(8010)    # Port Number
    tornado.ioloop.IOLoop.current().start()
