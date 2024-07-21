from flask import Flask, url_for, redirect

app = Flask(__name__)


# Add a home page
@app.route("/")
def home():
    return "<h1>This is the home page!</h1>"

# Add a score page with two path parameters 'name' (str) and 'marks' (int). 
# If marks < 30 redirect to 'fail' page otherwise 'pass' page.

@app.route("/score/<name>/<int:marks>")
def score(name,marks):
    if marks<30:
        return redirect(url_for("failed"))
    else:
        return redirect(url_for("passed"))
    

@app.route("/pass")
def passed():
    return "<h1>Congratulations! You have passed the exam</h1>"

@app.route("/fail")
def failed():
    return "<h1>Sorry! You have failed the exam</h1>"

if __name__=="__main__":
    app.run(debug=True)