from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return f"Welcom to the home page"

# Welcome with a path parameter
@app.route("/welcome/<name>")
def welcome(name):
    return f"Welcome, {name.title()}"

if __name__=="__main__":
    app.run(debug=True)