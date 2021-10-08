from pathlib import Path
from app import db
import enum
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey, null
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Path("db").mkdir(parents=True, exist_ok=True)


class Address(db.Model):
    db.__tablename__ = 'address'
    address_id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(120), nullable=False)
    street_no = db.Column(db.String(5), nullable=False)
    code = db.Column(db.String(7), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    customer = relationship("Customer", back_populates="address")

    def __repr__(self):
        return f"Address {self.street} {self.street_no}, {self.code} {self.city}"


class Customer(db.Model):
    db.__tablename__ = 'customer'
    customer_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.address_id'), nullable=False)
    codeActive = db.Column(db.Boolean)
    address = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User {self.email}"


pizza_to_toppings = db.Table('pizzas_to_toppings',
                             db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.pizza_id')),
                             db.Column('toppings_id', db.Integer, db.ForeignKey('toppings.toppings_id')))


class Pizza(db.Model):
    db.__tablename__ = 'pizza'
    pizza_id = db.Column(db.Integer, primary_key= True)
    pizza_name = db.Column(db.String(40),nullable = False)
    # toppings = relationship("Topping", back_populates="pizza")
    toppings = db.relationship('Toppings', backref='pizza', lazy='dynamic', secondary=pizza_to_toppings)

    def __repr__(self):
        return f"Pizza {self.pizza_name}, Toppings: {self.toppings}"
#
#
# def save_new_pizza(name, toppings):
#     new_pizza = Pizza(name=name)
#     db.session.add(new_pizza)
#     for i in range(1, len(toppings)):
#         # topping = find_single_topping(toppings.toppings_name)
#         topping = find_single_topping(name=toppings[i])
#         if topping is None:
#             return Exception(DatabaseError)
#         # new_pizza_topping = Pizza_Toppings(pizza_id=new_pizza.id, toppings_id=topping.id)
#         # db.session.add(new_pizza_topping)
#         db.session.commit()
#         # create topping Pizza link
#
#     new_menu_item = Menu(pizza_id=new_pizza.id)
#     db.session.add(new_menu_item)
#     db.session.commit()
#     return new_pizza



# class Pizza_Toppings(db.Model):
#     db.__tablename__='pizza_toppings'
#     pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.pizza_id'), nullable=False)
#     toppings_id = db.Column(db.Integer, db.ForeignKey('toppings.toppings_id'), nullable=False)
#

class Toppings(db.Model):
    db.__tablename__ = 'toppings'
    toppings_id = db.Column(db.Integer, primary_key=True)
    toppings_name = db.Column(db.String(40),nullable=False)
    toppings_price = db.Column(db.Float, nullable=False)
    toppings_vegi = db.Column(db.Boolean)
    pizza = relationship("Pizza", back_populates="toppings", secondary=Pizza_Toppings)

    def __repr__(self):
        return f"Toppings:{self.toppings_name}, Price:{self.toppings_price}, Vegi?{self.toppings_vegi}"


class Drinks(db.Model):
    db.__tablename__='drinks'
    drinks_id = db.Column(db.Integer, primary_key=True)
    drinks_name = db.Column(db.String(40), nullable=False)
    drinks_price = db.Column( db.Integer, nullable=False)

    def __repr__(self):
        return f"Drinks:{self.drinks_name},Price:{self.drinks_price}"


class Dessert(db.Model):
    db.__tablename__='dessert'
    dessert_id = db.Column(db.Integer, primary_key=True)
    dessert_name = db.Column(db.String(40), nullable=False)
    dessert_price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Dessert:{self.dessert_name},Price:{self.dessert_price}"


class Delivery_Driver(db.Model):
    db.__tablename__='delivery_driver'
    delivery_driver_id = db.Column(db.Integer, primary_key=True)
    delivery_driver_name = db.Column(db.String(20), nullable=False)
    delivery_driver_area = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Delivery driver name{self.delivery_driver_name}, delivered in this area{self.delivery_driver_area}"


driver_to_order_table = db.Table('driver_to_order',
                                 db.Column('order_id', db.Integer, db.ForeignKey('order.order_id'), primary_key=True),
                                 db.Column('driver_id', db.Integer, db.ForeignKey('delivery_driver.delivery_driver_id'),
                                           primary_key=True))

# class Order_Delivery(db.Model):
#     db.__tablename__='order_delivery'
#     order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
#     delivery_driver_id = db.Column(db.Integer, db.ForeignKey('delivery_driver.delivery_driver_id'))
#     delivery_driver = db.relationship('delivery_driver', backref=db.backref('order_delivery', lazy=True))
#     order = db.relationship('order', backref=db.backref('order_delivery', lazy=True))


class Menu(db.Model):
    db.__tablename__='menu'
    menu_id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.pizza_id'))
    drinks_id = db.Column(db.Integer, db.ForeignKey('drinks.drinks_id'))
    dessert_id = db.Column(db.Integer, db.ForeignKey('dessert.dessert_id'))
    # pizza = db.relationship('Pizza', backref=db.backref('menu', lazy=True))
    # drinks = db.relationship('Drinks', backref=db.backref('menu', lazy=True))
    # dessert = db.relationship('Dessert', backref=db.backref('menu', lazy=True))


class OrderEnum(enum.Enum):
    out_for_delivery = 1
    in_process = 2
    canceled = 3


class Order (db.Model):
    db.__tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(OrderEnum), nullable=False)
    placed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    discount = db.Column(db.Boolean)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    customer = db.relationship('Customer', backref=db.backref('order', lazy=True))

    def __repr__(self):
        return f"Order {self.order_id}, came in at {self.placed}, currently {self.status}, " \
               f"discount applied {self.discount}, entered by {self.customer_id}"


order_to_menu_table = db.Table('menu_to_order',
                               db.Column('order_id', db.Integer, db.ForeignKey('order.order_id')),
                               db.Column('menu_id', db.Integer, db.ForeignKey('menu.menu_id')))
# class Order_Menu(db.Model):
#     db.__tablename__='order_menu'
#     menu_id = db.Column(db.Integer, db.ForeignKey('menu.menu_id'),nullable=False)
#     order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'),nullable=False)
#     order = db.relationship('Order', backref=db.backref('order_menu', lazy=True))
#     menu = db.relationship('Menu', backref=db.backref('order_menu', lazy=True))


# db.drop_all()
db.create_all()
