from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class OrderCreation(FlaskForm):
    menu_field_list = []
    email = StringField('Email', validators=[DataRequired()])
    pizza_magarita = IntegerField("Margarita", default=0)
    pizza_buratina = IntegerField("Buratina", default=0)
    pizza_fungi = IntegerField("Fungi", default=0)
    pizza_parma = IntegerField("Parma", default=0)
    pizza_prosciutto = IntegerField("Prosciutto", default=0)
    pizza_pepperoni = IntegerField("Pepperoni", default=0)
    pizza_diavola = IntegerField("Diavola", default=0)
    pizza_salami = IntegerField("Salami", default=0)
    pizza_romana = IntegerField("Romana", default=0)
    pizza_napoli = IntegerField("Napoli", default=0)
    pizza_marinara = IntegerField("Marinara", default=0)
    pizza_crudo = IntegerField("Crudo", default=0)
    pizza_tricolore = IntegerField("Tricolore", default=0)
    water = IntegerField("Water", default=0)
    coke = IntegerField("Coke", default=0)
    apple = IntegerField("Apple Juice", default=0)
    orange = IntegerField("Orange Juice", default=0)
    white_wine = IntegerField("White Wine", default=0)
    red_wine = IntegerField("Red Wine", default=0)
    limoncello = IntegerField("Limoncello", default=0)
    espresso = IntegerField("Espresso", default=0)
    cappuccino = IntegerField("Cappuccino", default=0)
    tiramisu = IntegerField("Tiramisu", default=0)
    pana_cotta = IntegerField("Pana Cotta", default=0)
    tartufo = IntegerField("Tartufo", default=0)

    menu_field_list.append(pizza_magarita)
    menu_field_list.append(pizza_buratina)
    menu_field_list.append(pizza_fungi)
    menu_field_list.append(pizza_parma)
    menu_field_list.append(pizza_prosciutto)
    #menu_field_list.append(pizza_)

    submit = SubmitField('Sign Up')


"""
pizza_magarita 
pizza_caprese
pizza_buratina 
pizza_fungi 
pizza_parma 
pizza_prosciutto 
pizza_pepperoni
pizza_diavola 
pizza_salami 
pizza_romana 
pizza_napoli 
pizza_marinara 
pizza_crudo 
pizza_tricolore 

water 
coke 
apple 
orange
white_wine
red_wine 
limoncello 
espresso 
cappuccino

tiramisu 
pana_cotta 
tartufo
"""


