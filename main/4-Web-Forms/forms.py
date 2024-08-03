from flask_wtf import FlaskForm
from wtforms import (StringField, DateField, PasswordField,SubmitField, BooleanField, SelectField)
from wtforms.validators import (DataRequired, Length, Email, Optional,EqualTo, c)

# 1. Define a class "SignupForm" which extends the FlaskForm
class SignupForm(FlaskForm):

    # Add a username StringField with label "Username" and validators =[DataRequired(), Length(2,30)]
    username = StringField("Username", validators=[DataRequired(), Length(2,30)])
    

    # Add a email StringField with label "Email" and validators = [DataRequired(), Email()]; Validates an email address. 
    # Requires email_validator package to be installed. For ex: python pip install email-validator
    email = StringField("Email", validators=[DataRequired(),Email()])


    # Add a gender SelectField with label "Gender", choices=["Male", "Female", "Other"], and validators=[Optional()]
    gender = SelectField("Gender", choices=["Male","Female","Other"], validators=[Optional()])


    # Add a dob DateField with label "Date of Birth", and validators[Optional()]
    dob = DateField("Date of Birth", validators=[Optional()])


    # Add a password PasswordField with label "Password" and validators[DataRequired(), Length(5,25)]
    password = PasswordField("Password",validators=[DataRequired(),Length(5,25)])
    

    # Add a confirm password PasswordField with label "Confirm Password" and validators= [DataRequired(), Length(5, 25), EqualTo("password")]
    confirm_password = PasswordField("Confirm Password",validators=[DataRequired(),Length(5,25),EqualTo("password")])
    # Here the password in the EqualTo("password") is the password variable define just before the confirm_password

    # Add a submit SubmitField() with label "Sign Up"
    submit = SubmitField("Sign Up")



# Define a class "LoginForm" which extends the FlaskForm
class LoginForm(FlaskForm):

    # Add a email StringField with label "Email" and validators = [DataRequired(), Email()];
    email = StringField("Email",validators=[DataRequired(),Email()])
    

    # Add a password PasswordField with label "Password" and validators[DataRequired(), Length(5,25)]
    password = PasswordField("Password",validators=[DataRequired(),Length(5,25)])
    

    # Add a remember me BooleanField with Label "Remember Me"
    remember_me = BooleanField("Remember Me")

    # Add a submit SubmitField with label "Login"
    submit = SubmitField("Login")

# 2. layout.html