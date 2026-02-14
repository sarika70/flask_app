# 1. Create file → app.py

from flask import Flask

app = Flask(__name__)

@app.route("/") #Decorator
def hello():
    return "<h1 style='color: darkred; text-align:center'>Hellooooo Flask!!! 🎉</h1>"

@app.route("/about")
def about():
    return "<h2>This is my first Flask website :)</h2>"

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
# 1. Import the Flask class from the flask package
#    → This is the main building block we use to create web applications
#from flask import Flask

# 2. Create the Flask application instance
#    → __name__ is a special Python variable that tells Flask where to look 
#      for templates, static files, etc. (very useful when the app grows)
#app = Flask(__name__)

# 3. Define a route (URL path) using a decorator
#    → @app.route("/") means: when someone visits the root URL[](http://127.0.0.1:5000/)
#      this function will be called
#@app.route("/")
#def hello():
    # 4. The function returns HTML content directly
    #    → Flask will send this string as the response to the browser
    #    → You can return plain text, HTML, JSON, etc.
#    return "<h1 style='color: darkred; text-align:center'>Hellooooo Flask!!! 🎉</h1>"

# 5. Another route → different URL path
#    → Visiting http://127.0.0.1:5000/about will trigger this function
#@app.route("/about")
#def about():
    # Simple HTML response again
#    return "<h2>This is my first Flask website :)</h2>"

# 6. Standard Python idiom to check if this file is being run directly
#    → Prevents the server from starting when this file is imported as a module
#    → Very common pattern in Flask (and many other Python web frameworks)
#if __name__ == "__main__":
    # 7. Start the built-in development web server
    #    debug=True does three helpful things during learning:
    #      • auto-reloads when you save changes to the code
    #      • shows detailed error messages + interactive debugger in browser
    #      • prints useful logging information to the terminal
    #    → NEVER use debug=True in real production!
#    app.run(debug=True)    
    
### Steps to run the program 
## # 2. In terminal (same folder)
#pip install flask

# 3. Run it (two possible ways)
#flask run

# or
#python app.py