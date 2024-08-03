from flask import Flask, render_template, url_for
from employee import employees_data

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")
    # The title parameter is passed to the {{title}} variable in home.html --> layout.html



@app.route("/about")
def about():
    return render_template("about.html",title="About")


@app.route("/emp")
def emp():
    return render_template("emp.html",title="Employees",emps=employees_data)
# The emps parameter will send the employees_data (which is recieved from employees.py) to the emp.html as a path paramter.
# Note you can pass any parameter by defining it as a keyword parameter.

if __name__=="__main__":
    app.run(debug=True)