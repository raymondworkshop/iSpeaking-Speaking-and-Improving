"""
application factory 
*  a global Flask instance 
*  this is a package 

@wenlong 2019-03-11 
"""

import os

from flask import Flask
#from flask_socketio import SocketIO
#from flask_sslify import SSLify

#app = Flask(__name__)

#import flask.views

def create_app(test_config=None):
    # config an instance of Flask
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # database
        DATABASE=os.path.join(app.instance_path, 'ispeech.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    #socketio = SocketIO(app)
   
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    """
    @app.route('/')
    def index():
        return 'Index Page'
    """

    @app.route('/hello', methods=['GET', 'POST'])
    def hello():
        return "Hello, World!"

    # database
    from . import db
    db.init_app(app)

    
    # apply the blueprints to the app
    from . import auth, ispeech
    app.register_blueprint(auth.bp)
    app.register_blueprint(ispeech.bp)
    #app.register_blueprint(audio.bp)

    app.add_url_rule('/', endpoint='index')
    
    #sslify = SSLify(app)

    return app
