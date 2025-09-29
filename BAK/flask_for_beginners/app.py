from flask import Flask #imports core Flask class.

app = Flask(__name__) #creates Flask app instance. The __name__ argument tells Flask how to locate resources i.e.
                      #templates or static files
@app.route("/")     #reroute decorator. Tells Flask to run home() function whenever user visits website root URL (/)
def home():         #function that handles request to application's root URL
    return "Jesus Christ is Lord"