from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page!"

# We need two pages: If a student scores less than 30 then redirect it to fail page otherwise pass
# But we need a page where the student will enter his/her name and marks: named score

@app.route("/score/<name>/<int:marks>")
def score(name, marks):
    if marks < 30:
        # redirect student to fail page
        return redirect(url_for("failed"))
        # failed is the name of function which is associated with the fail page
    else:
        return redirect(url_for("passed"))
    

@app.route("/pass")
def passed():
    return "Congratulations! You have passed the exam!"

@app.route("/fail")
def failed():
    return f"Sorry, You have Failed the exam."


if __name__ == "__main__":
    app.run(debug=True)















    
