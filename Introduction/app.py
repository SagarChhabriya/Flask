from flask import Flask

# Create the flask app
app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return "This is Home Page"


# Start the app
if __name__ == "__main__":
    app.run(debug=True)