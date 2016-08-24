# coding:utf-8
import os
import sys
import time
import traceback

from flask import Flask
from flask import abort
from flask import redirect
from flask import render_template

from conf import *

app = Flask(__name__)


@app.route('/')
@app.route('/blog_list')
def blog_list():
    title = u"欢迎来访"
    return render_template("blog_list.html", **locals())


@app.route('/blog_content')
def blog_content(request):
    title = u""

    return render_template("blog_content.html", **locals())


@app.route('/blog_search')
def blog_search(request):
    title = u""

    return render_template("blog_search.html", **locals())


@app.route('/knowledge_list')
def knowledge_list(request):
    title = u"知识力量"

    return render_template("knowledge_list.html", **locals())


@app.route('/knowledge_content')
def knowledge_content(request):
    title = u""

    return render_template("knowledge_content.html", **locals())


if __name__ == '__main__':
    app.run(debug=DEBUG)
