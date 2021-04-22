#!/usr/bin/env python3
""" app main """

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """ class config """
    LANGUAGES = ['en', 'fr']

app.config.from_object(Config)

@app.route('/')
def basic_app():
    """ this is a basic app """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)