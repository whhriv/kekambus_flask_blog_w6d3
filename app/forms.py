from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, EqualTo


class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email Address', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log In')
    submit = SubmitField('Log In')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    body = TextAreaField('Body', validators=[InputRequired()])
    submit = SubmitField('Log In')
    