from flask_wtf import FlaskForm
#from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,TextField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextField('Message', validators=[DataRequired()])
    