# The whole code is same as url_redirection.py but the differnce is only how can we make dynamic urls?
# In simple words redirecting to the enpoints with parameters

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page!"

# We need two pages: If a student scores less than 30 then redirect it to fail page otherwise pass
# But we need a page where the student will enter his/her name and marks: named score

@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
         # Redirect to fail page
        return redirect( url_for("failed",sname=name,marks=num) )
         # Redirect to pass page
    else:
        return redirect( url_for("passed",sname=name,marks=num) )
    

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1>Congratz {sname.title()}, you've passed with {marks} marks!</h1>"

@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1>Sorry {sname.title()}, you've failed with {marks} marks!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
