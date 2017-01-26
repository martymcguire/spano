from .api import api
from . import extensions
from flask import Flask
import logging
import sys

def create_app(config_path='../spano.cfg'):
    app = Flask('spano')
    app.config.from_pyfile(config_path)
    configure_logging(app)
    extensions.init_app(app)
    app.register_blueprint(api)
    return app

def configure_logging(app):
    if app.debug:
        return

    app.logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
