#hello.py
import os
from flask import Flask, url_for, render_template
import stat_scraper

app = Flask(__name__)

#url_for('flot', filename='jquery.flot.js')

#everybody is a list of teams.  Each team is a dictionary.
everybody = stat_scraper.everybody

name = everybody

@app.route('/')
def hello():
	return render_template('basic.html', name=name)

@app.route('/nhl/')
def charts_scores():
	return render_template('nhl.html', teams=everybody)
		

#@app.route('/nhl/')

if __name__ == '__main__':
    app.run()