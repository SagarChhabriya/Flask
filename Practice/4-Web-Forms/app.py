# 3. Create a python file named "app.py"

# from forms import SignupForm, LoginForm
from forms import SignupForm, LoginForm
from flask import Flask, render_template

# Add a /home endpoint with title="Home" and render the template to "home.html"
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")


# Add a /signup endpoint with methods=["Get","Post"]
@app.route("/signup",methods=["GET","POST"])
def signup():
    form = SignupForm()
    return render_template("signup.html", title="SignUp",form=form)



# Add a form in "signup.html" with POST method. 
# Inside the body the endpoint /signup's method create an object of the SingupForm class named form. 
# Now define a variable in the parameters of the render_template() function and initialize 
# the local variable form with the object form. form=form. The form object is being send to the "signup.html"


# 4. signup.html