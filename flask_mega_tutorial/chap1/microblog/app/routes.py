from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    page_title = {'text': 'Life Expectancy Calculator'}
    demographics = [
        {'birth_year': 1970},
        {'state': 'VA'}, 
        {'county': 'Floyd'},
        {'value': 30},
        {'Race': 'White'},
        {'Sex': 'Male'}  
    ]
    return render_template('index.html', title='Home', page_title=page_title, demographics=demographics)