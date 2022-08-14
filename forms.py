from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """Form adding pet"""
    
    name = StringField(("Pet Name"), validators=[InputRequired()])
    species = SelectField("Species", choices=[("dog", "Dog"), ("cat", "Cat"), ("bird", "Bird")])
    photo = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Comments", validators=[Optional(), Length(min=10)])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Comments", validators=[Optional(), Length(min=10)])
    available = BooleanField("Availability")
