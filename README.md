Spano
=====

A minimum viable [Micropub](https://www.w3.org/TR/micropub/)
[Media Endpoint](https://www.w3.org/TR/micropub/#media-endpoint) implementation
built on Python, [Flask](http://flask.pocoo.org/) and
[Flask-HashFS](https://flask-hashfs.readthedocs.io/en/latest/). Uses
[Flask-IndieAuth](https://github.com/martymcguire/flask-indieauth/) to support
authentication with [IndieAuth](https://indieweb.org/IndieAuth).

Quick (&amp; Dirty) Start
-------------------------

How to run your own instance of Spano.

```bash
git clone https://github.com/martymcguire/spano.git
cd spano
```

Create and activate a virtualenv:

	virtualenv --python=/usr/bin/python3 venv
	source venv/bin/activate

or conda:

	conda create -n spano python=3.5
	source activate spano

Install required Python libraries

	pip install -r requirements.txt

Copy spano.cfg.template to spano.cfg and edit it to check the
values of `ME`, `TOKEN_ENDPOINT`

Run the dev server

	python run.py

You can test out the server with `curl`, but you'll need a valid
IndieAuth token to authenticate. One way to get one is to log in
with [Quill](https://quill.p3k.io/) and visit the
[Quill settings page](https://quill.p3k.io/settings), where you
can copy the access token.

To perform a test upload with `curl`:

	curl -D - -F "file=@myfile.jpg" \
	  -H"Authorization: Bearer xxxx..." \
	  localhost:5000/

You should see output like:

	HTTP/1.1 100 Continue

	HTTP/1.0 201 CREATED
	Content-Type: text/html; charset=utf-8
	Content-Length: 108
	Location: http://localhost:5000/cc/a5/97/7c/20049317385a31319590e39c8693638bb368767a76faf0735b6dd2cb.jpg
	Server: Werkzeug/0.11.4 Python/2.7.11
	Date: Thu, 26 Jan 2017 02:40:05 GMT

	File created: http://localhost:5000/cc/a5/97/7c/20049317385a31319590e39c8693638bb368767a76faf0735b6dd2cb.jpg

Deployment
----------

Spano needs a webserver like Apache or nginx for serving the actual file content,
and to act as a proxy for virtualhost support, HTTPS, etc.

These instructions are generic but hopefully a good starting place:

* [mod_wsgi for Apache](http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/)
* [uwsgi for nginx](http://flask.pocoo.org/docs/0.12/deploying/uwsgi/)

The Name?
---------

[Jessie Spano](https://en.wikipedia.org/wiki/List_of_Saved_by_the_Bell_characters#Jessie_Spano) was the most organized character on Saved by the Bell and the only one I would trust to keep my files in order.
