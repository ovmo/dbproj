from sqlalchemy import insert
from sqlalchemy.exc import DatabaseError

# from app import page_not_found
from db import db
from model.mysql_model import Pizza, Menu, Drinks, Dessert, Toppings, pizza_to_toppings


def find_single_menu(**kwargs):
    return Menu.query.filter_by(**kwargs).first()


def save_new_pizza(name, toppings):
    # if find_single_pizza(pizza_name=name) is not None:
    #     return None
    pizza_toppings = []
    # new_pizza = Pizza(pizza_name=name)
    # db.session.add(new_pizza)
    # db.session.commit()
    # committed_pizza = find_single_pizza(pizza_name=name)
    for i in range(0, len(toppings)):
        # topping = find_single_topping(toppings.toppings_name)
        topping = find_single_topping(toppings_name=toppings[i])
        pizza_toppings.append(topping)
        # stmt = (
        #     insert(pizza_to_toppings).values(pizza_id=committed_pizza.pizza_id, toppings_id=topping.toppings_id)
        # )
        # db.session.execute(stmt)
        # if topping is not None:

    new_pizza = Pizza(pizza_name=name, toppings=pizza_toppings)
    new_menu_item = Menu(pizza=new_pizza)
    # new_menu_item = Menu(pizza_id=committed_pizza.pizza_id)
    db.session.add(new_menu_item)
    db.session.commit()
    return new_pizza


def find_single_pizza(**kwargs):
    return Pizza.query.filter_by(**kwargs).first()


def is_pizza_vegi (**kwargs):
    pizza = find_single_pizza(**kwargs)
    Pizza.query.filter_by(Pizza.toppings.all())
    return


def save_new_toppings(name, price, vegi):
    # if find_single_topping(toppings_name=name) is not None:
    #     return None
    new_toppings = Toppings(toppings_name=name, toppings_price=price, toppings_vegi=vegi)
    db.session.add(new_toppings)
    db.session.commit()
    return new_toppings


def find_single_topping(**kwargs):
    return Toppings.query.filter_by(**kwargs).first()


def find_all_toppings(**kwargs):
    pizza = find_single_pizza(**kwargs)
    return Pizza.query.join(Pizza.toppings).filter_by(pizza_id=pizza.pizza_id).all()


def get_pizza_price(**kwargs):
    pizza = find_single_pizza(**kwargs)


def get_all_pizzas():
    return Pizza.query.all()


def save_new_drinks(name, price):
    # if find_single_drinks(drinks_name=name) is not None:
    #     return None
    new_drinks = Drinks(drinks_name=name, drinks_price=price)
    db.session.add(new_drinks)
    # committed_drink = find_single_drinks(drinks_name=new_drinks.drinks_name)
    new_menu_item = Menu(drinks=new_drinks)
    db.session.add(new_menu_item)

    return new_drinks


def find_single_drinks(**kwargs):
    return Drinks.query.filter_by(**kwargs).first()


def get_all_drinks ():
    return Drinks.query.all()


def save_new_desserts(name, price):
    # if find_single_dessert(dessert_name=name) is not None:
    #     return None
    new_dessert = Dessert(dessert_name=name, dessert_price=price)
    db.session.add(new_dessert)
    # db.session.commit()
    # committed_dessert = find_single_dessert(dessert_name=new_desserts.dessert_name)
    new_menu_item = Menu(dessert=new_dessert)
    db.session.add(new_menu_item)
    db.session.commit()
    return new_dessert


def find_single_dessert(**kwargs):
    return Dessert.query.filter_by(**kwargs).first()


def get_all_desserts():
    return Dessert.query.all()
