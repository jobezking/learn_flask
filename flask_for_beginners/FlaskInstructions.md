Flask Instructions. Presumes python3, python3-pip, python3-venv and Flask already installed. If not see https://github.com/jobezking/flask_for_beginners/blob/main/README.md

\#Step 1: Define Project and App folders and create the app package  
mkdir flask\_project; cd flask\_project; python3 \-m venv venv; source venv/bin/activate  
touch run.py config.py
mkdir app  
touch app/\_\_init\_\_.py app/routes.py

\#Step 2: Initialize the Flask app. This initializes the app and imports your routes. You will need this for the app to work correctly when Flask scans your app folder  
In app/\_\_init\_\_.py:  
from flask import Flask  
from config import Config

app \= Flask(\_\_name\_\_)  
app.config.from\_object(Config)

from app import routes

\#Step 3: Define a route. Inside app/[routes.py](http://routes.py):  
from flask import render\_template  
from app import app  
@app.route(“/”) 

def home():  
    return render\_template(“index.html”)

\#Step 4: Create the entry point. This file serves as your starting point. Instead of [app.py](http://app.py) you now run your application with python3 [run.py](http://run.py). Or if using Flask CLI:  
export FLASK\_APP=run.py  
flask run  
Inside run.py:  
from app import app

\#Step 5: configuration with [config.py](http://config.py). For better separation of concerns, keep config variables i.e. secret keys, database URIs etc. in [config.py](http://config.py). In [config.py](http://config.py):

import os  
class Config:  
    SECRET\_KEY=os.environ.get(‘SECRET\_KEY’) or ‘default\_secret’

\#Step 6: Add templates and Static folders.  
mkdir app/templates  
mkdir app/static  
touch app/templates/index.html  
In index.html:  
\<\!-- app/templates/index.html \--\>   
\<\!DOCTYPE html\>   
\<html\>   
\<head\> 	  
\<title\>Flask App\</title\>  
 \</head\>   
\<body\>  
\<h1\>Hello from Flask Template\!\</h1\>   
\</body\>   
\</html\>
