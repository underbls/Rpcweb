from wtforms import Form

from wtforms import DecimalField, IntegerField, StringField, FieldList, TextField

class LogForm(Form):
    """docstring for HelloForm."""
    name = StringField('name')
    passs = StringField('passs')

class ListHelloForm(Form):
    """docstring for SumForm."""
    name_movie = StringField('name_movie')
    date_p = StringField('date_p')
