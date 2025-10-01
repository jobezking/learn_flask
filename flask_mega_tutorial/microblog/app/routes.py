from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    page_title = {'text': 'Life Expectancy Calculator'}
    return render_template('index.html', title='Home', page_title=page_title)