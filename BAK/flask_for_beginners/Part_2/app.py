'''
#To run app
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=8080
#should see Running on http://127.0.0.1:5000 which you should open on your browser
'''
'''
Flask routes must return a string or a response object. 
Try to return an integer or list directly you get error.
'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return '<h1>Welcome to our homepage<h1>'
    
@app.route('/about')
def about():
    return '<p>About us: Jesus Christ Is Lord<p>'
    
@app.route('/contact')
def contact():
    return '<p>Contact us at hello@example.com<p>'
    
@app.route('/services')
def services():
    return 'Here are our services'
    
@app.route('/blog')
@app.route('/blog/')
def blog():
    return 'Welcome to the blog'
    
@app.route('/welcome')
def welcome():
    return '''
        <h1>Welcome!</h1>
        <p>Thanks for visiting our site.</p>
    '''