from app import db
from model.mysql_model import Pizza, Pizza_Toppings, Menu

def save_new_pizza(name, toppings):
    new_pizza = Pizza(name=name)
    db.session.add(new_pizza)
    for i in range(1, len(toppings)):
        # topping = find_single_topping(toppings.toppings_name)
        topping = find_single_topping(toppings[i])
        if topping is None:
            return Exception(DatabaseError)
        new_pizza_topping = Pizza_Toppings(pizza_id=new_pizza.id, toppings_id=topping.id)
        db.session.add(new_pizza_topping)
        db.session.commit()
        # create topping Pizza link

    new_menu_item = Menu(pizza_id=new_pizza.id)
    db.session.add(new_menu_item)
    db.session.commit()
    return new_pizza


def find_single_pizza(**kwargs):
    return Pizza.query.filter_by(**kwargs).first()

def find_all_toppings(**kwargs):
    return Pizza.query.filter()

def is_pizza_vegi (**kwargs):
    return



