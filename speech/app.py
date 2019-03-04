# -*- coding: utf-8 -*-
"""
a web-based system to improve English (word) pronouncation, and give a marker

@author wenlong

"""

from flask import Flask

app = Flask(__name__)

#
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return "Hello, World!"


#main
if __name__ == '__main__':
    app.run(debug=True)

#