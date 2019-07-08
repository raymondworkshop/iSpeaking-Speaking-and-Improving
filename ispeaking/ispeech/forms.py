# -*- coding: utf-8 -*-
"""
@author raymon
"""

from flask_wtf import Form
from wtforms import TextField, IntegerField, SubmitField, RadioField, SelectField, SelectMultipleField, widgets, validators, ValidationError

class LoginForm(Form):
    username=TextField('username', [validators.Length(min=4, max=25)])
    password= PasswordField('password',[validators.DataRequired()])
    algs  = RadioField('The language:', choices = [(0, 'English'), (1, 'Cantonese'), (2, 'Mandarin')], default=0)
    submit = SubmitField('Submit')

AVAILABLE_CHOICES = [ (0,'English'),
                      (1,'Cantonese'),
                      (2,'Mandarin')]

# The function is replaced by database
class EntryForm(Form):
    #text=TextField('input', [validators.Length(min=4, max=25)])
    words=StringField('password', [validators.Length(min=4, max=25)])
    password= PasswordField('password')
    #wordinput = TextField('wordinput')
    cselect = RadioField('The language:', choices = [(0, 'English'), (1, 'Cantonese'), (2, 'Mandarin')], default=0)

    submit =SubmitField("Submit")