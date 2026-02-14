from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jayant Kumar'}
    page_name = 'error.html'
    if user: 
       page_name = 'index.html'
    return render_template(page_name, title='Home', user_name=user)# RHS user is the one defined before
    
if __name__ == "__main__":
    app.run(debug=True)

### Steps to run the program 
## # 2. In terminal (same folder)
#pip install flask

# 3. Run it (two possible ways)
#flask run

# or
#python app.py    