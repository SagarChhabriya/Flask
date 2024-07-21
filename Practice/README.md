# Exercises

## 1-2 Introduction and Redirection

1. Simple App

   - Add a home page
   - Add a welcome page
   - Add a path parameter to welcome page
   - Add a page 'add' with 2 numerical path parameters which returns the sum of parameters.

2. Dynamic URL

   - Add a page with path parameter 'name' and greets.

3. URL Redirection

   - Add a Home Page
   - Add a score page with two path parameters 'name' (str) and 'marks' (int). If marks < 30 redirect to 'fail' page otherwise 'pass' page.

4. URL Building
   - Add a home page
   - Add 'score' page with redirection to 'fail' and 'pass' pages. The parameters name and marks of score should be send/passed/shared to fail and pass pages.

## 3 Jinja-Inheritence

1. Add a "layout.html" containing the boiler-plot code for inheritence inside the folder "templates"
   - Add a jinja block "content"
   - Add a title variable
2. Create html pages inside the folder "templates"
   - home, about, emp
3. Create a file named emp.py which contains a 4 nested python dictionary. (outside the templates folder)
   Ex:
   ```python
   employees_data = {
    1: {
        "name": "Michael",
        "age": 42,
        "position": "Manager",
    },
   ```
   - import the emp.py data in app.py and pass it to emp.html as a paramter in render_templated() function.<br><br>
     `Hint`
   ```python
   {% extends "layout.html" %}
   {% block content%}
      {% for employee_id, employee_info in data.items() %}
            <li>
                <strong>Employee ID:</strong> {{ employee_id }}<br>
                <strong>Name:</strong> {{ employee_info.name }}<br>
                <strong>Age:</strong> {{ employee_info.age }}<br>
                <strong>Position:</strong> {{ employee_info.position }}<br>
            </li>
        <br>
      {% endfor %}
   {% endblock%}
   ```

## 4 - Web Forms

1.  Create a file named "forms.py"

    - from flask_wtf import FlaskForm (pip install flask-wtf)
    - Define a class "SignupForm" which extends the FlaskForm

      - Add a username StringField with label "Username" and validators =[DataRequired(), Length(2,30)]
      - Add a email StringField with label "Email" and validators = [DataRequired(), Email()]; Validates an email address. Requires email_validator package to be installed. For ex: ` python pip install email-validator`
      - Add a gender SelectField with label "Gender", choices=["Male", "Female", "Other"], and validators=[Optional()]
      - Add a dob DateField with label "Date of Birth", and validators[Optional()]
      - Add a password PasswordField with label "Password" and validators[DataRequired(), Length(5,25)]
      - Add a confirm password PasswordField with label "Confirm Password" and validators= [DataRequired(), Length(5, 25), EqualTo("password")]
      - Add a submit SubmitField() with label "Sign Up"

    - Define a class "LoginForm" which extends the FlaskForm
      - Add a email StringField with label "Email" and validators = [DataRequired(), Email()];
      - Add a password PasswordField with label "Password" and validators[DataRequired(), Length(5,25)]
      - Add a remember me BooleanField with Label "Remember Me"
      - Add a submit SubmitField with label "Login"

    ### `Hint`

    ```python
    from wtforms import (
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
    )
    ```

    <br><br>

    ```python
    from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
    )
    ```

2.  Create files "layout.html", "home.html", "login.html", and "signup.html" inside the templates folder.

    - Add a title variable in layout.html
    - Add a block named content in layout.html

3.  Create a python file named "app.py"

    - from forms import SignupForm, LoginForm
    - Add a /home endpoint with title="Home" and render the template to "home.html"
    - Add a /signup endpoint with methods=["Get","Post"]
      ```text
      The Get Method is used to query the data or get the data and the post mehtod is used to send the data. To use the POST method first we need to use the Get method later this will be defined for now just follow the instructions.
      ```
    - Add a form in "signup.html" with POST method. Inside the body the endpoint /signup's method create an object of the SingupForm class named form. Now define a variable in the parameters of the render_template() function and initialize the local variable form with the object form. form=form. The form object is being send to the "signup.html"

4.  Signup.html

    - extend the layout.html
    - Define the body of signup.html's form inside the content block.
      - Content Block > html form > div
      - Add a div for the username lable and field.
        Ex:
      ```python
      {{form.username.label}} # Label
      {{form.username}}       # Field
      ```
      ```text
      The SignupForm class is defined in the forms.py. The SignupForm and LoginForm class of forms module is imported in the app.py. Inside the singup() method's body an object of the SignupForm class is created and passed to the signup.html as a parameter inside the parantheses of the render_template() function.
      ```
      - Add div(s) for each Field defined in the SignupForm > forms.py
        - username, email, gender, dob, password, confirm_password
        - At last call the submit {{form.submit()}}
    - Now execute the application you will get an error
      ```python
      RuntimeError: A secret key is required to use CSRF.
      ```

    ````text
    You are getting this error because the wtforms library requires the CSRF (Cross site request forgery) to be handled. In simple the error states that you need to pass a CSRF token. Now head towards the app.py and this line after create the app object:
    ```python
    app.config["SECRET_KEY] = "this_is_a_secret_key"
    ````

    Where the app is Flask class object and you need to add the secret key value/token. For now you can use the same line of code for the learning purpose.

    ````
    - Remember the the /singup endpoint with methods ["Get", "POST"] if you don't define this list inside the parantheses of /signup decorater you will get an error when you click the submit button:
    ```python
    Method Not Allowed
    The method is not allowed for the requested URL.
    ````

    This error occurs because the data is recieved "GET" from the fields of web form but where to send this data? So this why you need to define the "POST" in the decorater /signup and to use the "POST" the "GET" is required.

5.  app.py
    ```python
    if form.validate_on_submit
       flash(f"Successfully Registered {form.username.data}!")
       return render_template("signup.html",title="Sign Up", form=form)
    ```
