from flask import Flask, render_template
from emp import employees_data

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/emp")
def emp():
    return render_template("emp.html",title="Employees", data=employees_data)

if __name__ == "__main__":
    app.run(debug=True)
