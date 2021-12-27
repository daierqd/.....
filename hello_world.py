#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return f'<h1>Helloworld!</h1>'


if __name__ == '__main__':

    app.run()
    pass
