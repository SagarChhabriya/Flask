# Flask App Routing

from flask import Flask, request

# Create a simple flask application
app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "Welcome!"

@app.route("/index",methods=["GET"])
def index():
    return "Welcome to the Index Page"


# Variable Rule
@app.route("/success/<int:score>")
def success(score):
    return "The Person has passed and the score is: "+str(score)

@app.route("/fail/<int:score>")
def success(score):
    return "The person has failed and the score is: "+str(score)

@app.route("/form",methods=["GET","POST"])
def form():
    if 


if __name__=="__main__":
    app.run(debug=True)