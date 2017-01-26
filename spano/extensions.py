from flask_hashfs import FlaskHashFS

fs = FlaskHashFS()

def init_app(app):
  fs.init_app(app)
