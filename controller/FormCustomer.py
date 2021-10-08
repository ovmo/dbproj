from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CustomerCreation(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    street_no = StringField('House Number', validators=[DataRequired()])
    area_code = StringField('Postal Code', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    submit = SubmitField('Sign Up')