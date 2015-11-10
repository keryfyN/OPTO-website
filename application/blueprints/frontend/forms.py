# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import SubmitField, TextAreaField
from wtforms.validators import InputRequired, Email
from wtforms_html5 import EmailField, TextField

class ContactForm(Form):
    name = TextField("Name", validators=[InputRequired('Please enter your name.')])
    subject = TextField("Subject")
    email = EmailField("Email",  validators=[InputRequired("Please enter your email address."), Email("Please enter your email address.")])
    message = TextAreaField("Message", validators=[InputRequired('Please enter your message.')])
    submit = SubmitField("Send")
