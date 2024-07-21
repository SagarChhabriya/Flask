from flask import Flask, redirect, url_for

app = Flask(__name__)

# Add a home page
@app.route("/")
def home():
    return "<h1>This is the home page!</h1>"


# Add 'score' page with redirection to 'fail' and 'pass' pages. 
# The parameters name and marks of score should be send/passed/shared to fail and pass pages.

@app.route("/score/<name>/<int:marks>")
def score(name, marks):
    if marks<30:
        return redirect(url_for("failed", name=name, marks=marks))
    else:
        return redirect(url_for("passed", name=name, marks=marks))
    
# Note: Keyword parameters are necessary otherwise the exception will occur.


@app.route("/pass/<name>/<int:marks>")
def passed(name,marks):
    return f"<h1>Congratulations {name.title()}! You have passed the exam with {marks} marks. </h1>"

@app.route("/fail/<name>/<int:marks>")
def failed(name,marks):
    return f"<h1>Sorry {name}. You have failed the exam with {marks} marks</h1>"


if __name__=="__main__":
    app.run(debug=True)