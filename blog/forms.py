"""
FORMS
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=2, max=20)
    ])

    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])

    password = PasswordField('Password', validators=[
        DataRequired()
    ])

    confirm_password = PasswordField('Comfirm Password', validators=[
        DataRequired(),
        EqualTo('password')
    ])

    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username).first()

        if user:
            raise ValidationError("The username is already taken")

    def validate_email(self, email):
        user = User.query.filter_by(email=email).first()

        if user:
            raise ValidationError("The username is already in use")


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])

    password = PasswordField('Password', validators=[
        DataRequired()
    ])

    remember_me = BooleanField('Remember me')

    submit = SubmitField('Sign in')
