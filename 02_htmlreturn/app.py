from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jayant'}
    return '''
<html>
    <head>
        <title>Home Page - Myblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
        <p> Please all add this to the html </p>
    </body>
</html>'''

if __name__ == "__main__":
    app.run(debug=True)

### Steps to run the program 
## # 2. In terminal (same folder)
#pip install flask

# 3. Run it (two possible ways)
#flask run

# or
#python app.py