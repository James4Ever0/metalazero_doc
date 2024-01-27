import tornado.ioloop
import tornado.web
import os

os.system("ifconfig")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
#        print(dir(self.request))
        ip = self.request.remote_ip
        print("request from:",ip)
        self.write("Hello, world")
 
    def make_app():
        return tornado.web.Application([ (r"/", MainHandler), ])  # URL Mapping
 
if __name__ == "__main__":
    app = MainHandler.make_app()
    app.listen(8888)    # Port Number
    tornado.ioloop.IOLoop.current().start()
