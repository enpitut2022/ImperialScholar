# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World && ココロミエル'

if __name__ == '__main__':
    app.run()