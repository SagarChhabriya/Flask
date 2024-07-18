from flask import Flask

app = Flask(__name__)

# Add a home page
@app.route("/")
def home():
    return "<h1>This is the home page!</h1>"


# Add a welcome page, Add a path parameter to the welcome page
# ValueError: URL rule 'welcome/<name>' must start with a slash.
@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hi {name.title()}! This is the welcome page!</h1>"

# Add a 'add' page with 2 parameter which returns the sum of parameters
@app.route("/add/<int:num1>/<int:num2>")
def add(num1,num2):
    return f"<h1>Sum of {num1} and {num2} is {num2+num1} </h1>"


if __name__ == "__main__":
    app.run(debug=True)