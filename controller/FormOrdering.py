from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class OrderCreation(FlaskForm):
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

    pizza_field_list = []
    drink_field_list = []
    dessert_field_list = []

    pizza_field_list.append(pizza_magarita)
    pizza_field_list.append(pizza_buratina)
    pizza_field_list.append(pizza_fungi)
    pizza_field_list.append(pizza_parma)
    pizza_field_list.append(pizza_prosciutto)
    pizza_field_list.append(pizza_pepperoni)
    pizza_field_list.append(pizza_diavola)
    pizza_field_list.append(pizza_salami)
    pizza_field_list.append(pizza_romana)
    pizza_field_list.append(pizza_napoli)
    pizza_field_list.append(pizza_marinara)
    pizza_field_list.append(pizza_crudo)
    pizza_field_list.append(pizza_tricolore)

    drink_field_list.append(water)
    drink_field_list.append(coke)
    drink_field_list.append(apple)
    drink_field_list.append(orange)
    drink_field_list.append(white_wine)
    drink_field_list.append(red_wine)
    drink_field_list.append(limoncello)
    drink_field_list.append(espresso)
    drink_field_list.append(cappuccino)

    dessert_field_list.append(tiramisu)
    dessert_field_list.append(pana_cotta)
    dessert_field_list.append(tartufo)

    submit = SubmitField('Order Now')

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


