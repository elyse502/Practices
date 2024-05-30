#!/home/elysee_niyibizi/Practices/python/UDEMY/flask/flaskenv/bin/python3
# Tutorial 61-Flask WTF Extension

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField("Name Of Student", [DataRequired("Please enter your name.")])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField("Address")
    email = StringField("Email Address", [DataRequired("Please enter your email address."), Email("Please enter a valid email address.")])
    Age = IntegerField("age")
    language = SelectField('Languages', choices=[('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("Send")