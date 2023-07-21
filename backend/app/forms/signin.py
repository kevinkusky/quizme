from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class SigninForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    signin = SubmitField('Sign In')
