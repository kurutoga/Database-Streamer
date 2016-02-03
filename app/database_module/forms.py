from flask.ext.wtf import Form
from wtforms.fields.html5 import DateField
from wtforms import SubmitField

class DateForm(Form):
    startDate = DateField('From')
    endDate   = DateField('To')
    submit    = SubmitField('Download')
