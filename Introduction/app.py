from flask import Flask

# Create the flask app
app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return "This is Home Page"


# Add a path paramter in a page
@app.route("/welcome/<name>")
def welcom(name):
    return f"Hello {name}, Welcome to our website!"

# Input URL Ex: http://127.0.0.1:5000/welcome/ok
# Output: Hello ok, Welcome to our website!


# Add a integer path parameter
@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return f"The sum of {num1} and {num2} is {num2+num1}"
# Start the app
if __name__ == "__main__":
    app.run(debug=True)