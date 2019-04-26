#!/usr/bin/env python
import sys
import logging
import pyodbc 

from flask import Flask
from flask import render_template

app = Flask(__name__)

logging.basicConfig(format='%(asctime)s:%(filename)s:%(levelname)s:%(message)s', filename='logs/NXHello.log', level=logging.DEBUG)

class Foo():

    def __init__(self):
        logging.info(__name__)
        self.name = None

@app.route('/')
def index():
    foo = Foo()
    logging.info(id(foo))
    logging.info('Hello, World!')
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<foo>')
def hello(foo=None):
    return render_template('hello.html', foo=foo)
    
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'