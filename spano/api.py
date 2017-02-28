from .extensions import fs
from flask import request, Response, Blueprint
from flask_hashfs import FlaskHashFS
from flask_indieauth import requires_indieauth
import mimetypes

api = Blueprint('api', __name__)

@api.route('/', methods=['POST'])
@requires_indieauth
def publish():
    if not 'file' in request.files:
        return Response("Invalid request.", 400)
    else:
        f = request.files['file']
        f_ext = guess_extension(f)
        address = fs.put(f, extension=f_ext)
        url = fs.url_for(address.relpath)
        resp = Response ("File created: %s" % url, 201)
        resp.headers['Location'] = url
        return resp

def guess_extension(f):
    ext = mimetypes.guess_extension(f.mimetype)
    ext = '.jpg' if (ext == '.jpe') else ext
    ext = '.mp3' if (f.mimetype == 'audio/mp3') else ext
    return ext
