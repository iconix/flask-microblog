from flask.ext.wtf import Form # http://wtforms.readthedocs.org/en/latest/
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
	openid = TextField('openid', validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)