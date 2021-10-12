from app import db
from model.mysql_model import Pizza, Pizza_Toppings, Menu

def find_single_menu(**kwargs):
    return Menu.query.filter_by(**kwargs).first()


def save_new_pizza(name, toppings):
    pizza_toppings = []
    for i in range(1, len(toppings)):
        # topping = find_single_topping(toppings.toppings_name)
        topping = find_single_topping(toppings[i])
        if topping is None:
            return Exception(DatabaseError)
        else:
            pizza_toppings.append(topping)
    new_pizza = Pizza(name=name, pizza_toppings)
    db.session.add(new_pizza)
    new_menu_item = Menu(pizza_id=new_pizza.id)
    db.session.add(new_menu_item)
    db.session.commit()
    return new_pizza


def find_single_pizza(**kwargs):
    return Pizza.query.filter_by(**kwargs).first()

def find_all_toppings(**kwargs):
    pizza = find_single_pizza(**kwargs)
    return Pizza.query.filter(Pizza.query.all())

def is_pizza_vegi (**kwargs):
    return Pizza.query

def save_new_drinks(name,price):
    new_drinks = Drinks(drinks_name=name, drinks_price=price)
    new_menu_item = Menu(drinks_id=new_drinks.id)
    db.session.add(new_menu_item)
    db.session.add(new_drinks)
    db.session.commit()
    return new_drinks


def find_single_drinks(**kwargs):
    return Drinks.query.filter_by(**kwargs).first()


def save_new_desserts(name,price):
    new_desserts = Dessert(dessert_name=name, dessert_price=price)
    new_menu_item = Menu(dessert_id=new_desserts.id)
    db.session.add(new_menu_item)
    db.session.add(new_desserts)
    db.session.commit()
    return new_desserts


def find_single_dessert(**kwargs):
    return Dessert.query.filter_by(**kwargs).first()



