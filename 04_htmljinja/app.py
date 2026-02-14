from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/') # URI or end points
@app.route('/index')
def index(): # view function 
    user = {'username': 'Jayant Kumar'}
    courses = [
        {
            'trainer': {'trainername': 'Jayant Kumar'},
            'details': 'Welcome to Flask!'
        },
        {
            'trainer': {'trainername': 'Jayant Kumar M'},
            'details': 'Data Science with GenAI & Agentic AI!'
        }
    ]
    return render_template('index.html', title='Home', user_all=user, courses_all=courses)
    
if __name__ == "__main__":
    app.run(debug=True)

### Steps to run the program 
## # 2. In terminal (same folder)
#pip install flask

# 3. Run it (two possible ways)
#flask run

# or
#python app.py        