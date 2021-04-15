from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, NumberRange, URL

species = ["Cat", "Dog", "Guinea Pig"]


class AddPet(FlaskForm):

    name = StringField('Name', validators=[InputRequired()])

    species = SelectField('Species', choices=[(sp, sp) for sp in species])

    photo_url = StringField("Add Photo URL", validators=[URL(
        require_tld=True, message='URL invalid, please try again')])

    age = IntegerField('Age', validators=[NumberRange(
        min=0, max=30, message='Only pets from 0 to 20 old are accepted')])
    
    notes = TextAreaField('Type notes here')