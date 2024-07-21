# Add a page with path parameter 'name' and greets.

from flask import Flask

app = Flask(__name__)

# Add a home page
@app.route("/")
def home():
    return "<h1>This is the home page!</h1>"

# Add welcome page with path parameter
@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>RADHE RADHE {name.title()} 🙏🏼 this is the home page!</h1>"

if __name__=="__main__":
    app.run(debug=True)
