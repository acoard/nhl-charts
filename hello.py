#hello.py
import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Whattup world?'

if __name__ == '__main__':
    app.run()