from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class WordForm(Form):
    word_field = StringField('word', validators=[DataRequired()])
