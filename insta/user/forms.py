from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField


class SignUpForm(FlaskForm):
    username = StringField('User Name', [validators.DataRequired(), validators.Length(min=2, max=25)])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=2, max=15)])
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired(), validators.EqualTo('password')])
    submit = SubmitField('Create Account')


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=2, max=15)])
    submit = SubmitField('Login')


class SaveButtonForm(FlaskForm):
    savePhoto = SubmitField('save')

