"""
@raymond 07-05-2019
"""


import os
import sys
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.wsgi
import wave
import uuid
import gc
from opus.decoder import Decoder as OpusDecoder

#
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#
#from app import app
"""
from jinja2 import  Environment, FileSystemLoader
# Load template file templates/site.html
TEMPLATE_FILE = "index.html"
templateLoader = FileSystemLoader( searchpath="templates/" )
templateEnv = Environment( loader=templateLoader )
template = templateEnv.get_template(TEMPLATE_FILE)
"""

class OpusDecoderWS(tornado.websocket.WebSocketHandler):
    
    def open(self):

        print('new connection')
        self.initialized = False

    def my_init(self, msg) :

        print(msg)
        rate, is_encoded, op_rate, op_frm_dur = [int(i) for i in msg.split(',')]
        #rate : actual sampling rate
        #op_rate : the rate we told opus encoder
        #op_frm_dur : opus frame duration

        filename = str(uuid.uuid4()) + '.wav'

        wave_write = wave.open(filename, 'wb')
        wave_write.setnchannels(1)
        wave_write.setsampwidth(2) #int16, even when not encoded
        wave_write.setframerate(rate)

        if self.initialized :
            self.wave_write.close()

        self.is_encoded = is_encoded
        self.decoder = OpusDecoder(op_rate, 1)
        self.frame_size = op_frm_dur * op_rate
        self.wave_write = wave_write
        self.initialized = True

    def on_message(self, data) :

        if str(data).startswith('m:') :
            self.my_init(str(data[2:]))
        else :
            if self.is_encoded :
                pcm = self.decoder.decode(data, self.frame_size, False)
                self.wave_write.writeframes(pcm)

                # force garbage collector
                # default rate of cleaning is not sufficient
                gc.collect()

            else :
                self.wave_write.writeframes(data)

    def on_close(self):

        if self.initialized :
            self.wave_write.close()

        print('connection closed')

"""
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("www/index.html")
"""

class Hello(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello")

#index_output = template.render(title="Speaking & Improving")
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("www/index.html")
        


class RecordHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("record.html")


#import jinja2
#jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template/path/'), autoescape=False)
#jinja2_loader = Jinja2Loader(jinja2_env)

# Give it to Tornado to replace the default Loader.
settings = { 
    #"template_path": os.path.join(os.path.dirname(__file__), "www"),
    #"static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True,
    "autoreload": True,
    }

application = tornado.web.Application([
    (r'/hello', Hello),
    (r'/ws', OpusDecoderWS),
    (r'/', MainHandler),
    #(r'/record', RecordHandler),
    (r'/(.*)', tornado.web.StaticFileHandler, { 'path' : './www' }),
    #(r'.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
    ], **settings)

if __name__ == "__main__":
    """
    wsgi_app = tornado.wsgi.WSGIContainer(app)


    application = tornado.web.Application([
    (r'/ws', OpusDecoderWS),
    #(r'/', MainHandler),
    #(r'/(.*)', tornado.web.StaticFileHandler, { 'path' : './www' }),
    (r'.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
    ], **settings)
    """

    http_server = tornado.httpserver.HTTPServer(application)

    http_server.listen(int(os.environ.get('PORT', 8888)))
    print('http server started')
    tornado.ioloop.IOLoop.instance().start()
