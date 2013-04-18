#hello.py
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack
import stat_scraper
from sqlite3 import dbapi2 as sqlite3

app = Flask(__name__)
app.debug = True

'''
Current State of Affairs:

ESPN requires a special partner status to get their live stats, and it appears 
they obsfucate just scrapping them from the site.  Need to do some googling
to see if getting around this is possible.



'''


@app.route('/')
def hello():
	return render_template('basic.html', name=name)

@app.route('/nhl/')
def charts_scores():
	stat_scraper.write_json()
	return render_template('nhl.html', teams=stat_scraper.everybody, 
						last_modified=stat_scraper.age_of_json())

@app.route('/test/')
def test_page():
	return render_template('test.html')



if __name__ == '__main__':
    app.run()