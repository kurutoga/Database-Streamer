from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField
from wtforms.validators import Email, EqualTo
from wtforms.validators import Required

class LoginForm(Form):
    name = TextField('Name', [Required(message='Provide a name, please!')])
    password = PasswordField('Password', [Required(message='Must provide a password.')])

class SignupForm(Form):
    name = TextField('Name', [Required(message='Required Field!')])
    email = TextField('Email', [Email(), Required(message='Forgot email?')])
    password = PasswordField('Password', [Required(message='Password is essential')])
    repeat  = PasswordField('Repeat Password', [Required(), EqualTo('password', message='Password must match!.')])
    tbname = TextField('tbname', [Required()])
