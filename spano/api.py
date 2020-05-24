from .extensions import fs
from flask import request, Response, Blueprint
from flask_hashfs import FlaskHashFS
from flask_indieauth import requires_indieauth
import mimetypes
import magic
import json
import os

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
        resp = Response ( json.dumps({'url': url}), 201 )
        resp.headers['Content-type'] = 'application/json'
        resp.headers['Location'] = url
        return resp

def guess_extension(f):
    m = magic.Magic(mime=True)
    content = f.stream.read(1024)
    mimetype = m.from_buffer(content)
    ext = mimetypes.guess_extension(mimetype)
    ext = '.jpg' if (ext == '.jpe') else ext
    ext = '.mp3' if (f.mimetype == 'audio/mp3') else ext
    ext = '.txt' if (f.mimetype == 'text/plain') else ext
    # sometimes we have to trust the extension we're given?
    if (f.mimetype == 'application/octet-stream'):
        fname, ext = os.path.splitext(f.filename)
    #raise ValueError(mimetype)
    return ext
