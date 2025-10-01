from app import app

@app.route('/')
@app.route('/index')
def index():
    page_title = {'text': 'Life Expectancy Calculator'}
    return '''
    <html>
        <head>
            <title>Home Page - Life Expectancy Calculator</title>
        </head>
        <body>
            <h3>''' + page_title['text'] + '''</h3>
        </body>
    </html>'''