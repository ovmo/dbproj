from pathlib import Path
from db import db
import enum
from datetime import datetime
from sqlalchemy.orm import relationship

Path("db").mkdir(parents=True, exist_ok=True)


class Address(db.Model):
    db.__tablename__ = 'address'
    address_id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(120), nullable=False)
    street_no = db.Column(db.String(5), nullable=False)
    code = db.Column(db.String(7), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    customer = relationship("Customer", back_populates="address", cascade="all, delete")

    def __repr__(self):
        return f"Address {self.street} {self.street_no}, {self.code} {self.city}"


class Customer(db.Model):
    db.__tablename__ = 'customer'
    customer_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.address_id'), nullable=False)
    codeActive = db.Column(db.Boolean)
    address = relationship("Address", back_populates="customer", cascade="all, delete")
    order = db.relationship('Order', back_populates='customer', cascade="all, delete")

    def __repr__(self):
        return f"User {self.email}"


pizza_to_toppings = db.Table('pizza_to_toppings',
                             db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.pizza_id')),
                             db.Column('toppings_id', db.Integer, db.ForeignKey('toppings.toppings_id')))
# class PizzaToToppings(db.Model):
#     db.__tablename__ = 'pizza_to_toppings'
#     pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.pizza_id'), nullable=False, primary_key=True)
#     toppings_id = db.Column(db.Integer, db.ForeignKey('toppings.toppings_id'), nullable=False, primary_key=True)


class Pizza(db.Model):
    db.__tablename__ = 'pizza'
    pizza_id = db.Column(db.Integer, primary_key=True)
    pizza_name = db.Column(db.String(40), nullable=False)
    # toppings = relationship("Topping", back_populates="pizza")
    toppings = db.relationship('Toppings', back_populates="pizza", lazy='dynamic', secondary='pizza_to_toppings', cascade="all, delete")
    menu = db.relationship('Menu', back_populates='pizza', cascade="all, delete")


    def __repr__(self):
        return f"Pizza {self.pizza_name}, Toppings: {self.toppings}"


class Toppings(db.Model):
    db.__tablename__ = 'toppings'
    toppings_id = db.Column(db.Integer, primary_key=True)
    toppings_name = db.Column(db.String(40),nullable=False)
    toppings_price = db.Column(db.Float, nullable=False)
    toppings_vegi = db.Column(db.Boolean)
    pizza = relationship("Pizza", back_populates="toppings", lazy='dynamic', secondary='pizza_to_toppings', cascade="all, delete")

    def __repr__(self):
        return f"Toppings:{self.toppings_name}, Price:{self.toppings_price}, Vegi?{self.toppings_vegi}"


class Drinks(db.Model):
    db.__tablename__ = 'drinks'
    drinks_id = db.Column(db.Integer, primary_key=True)
    drinks_name = db.Column(db.String(40), nullable=False)
    drinks_price = db.Column( db.Integer, nullable=False)
    menu = db.relationship('Menu', back_populates='drinks', cascade="all, delete")

    def __repr__(self):
        return f"Drinks:{self.drinks_name},Price:{self.drinks_price}"


class Dessert(db.Model):
    db.__tablename__='dessert'
    dessert_id = db.Column(db.Integer, primary_key=True)
    dessert_name = db.Column(db.String(40), nullable=False)
    dessert_price = db.Column(db.Integer, nullable=False)
    menu = db.relationship('Menu', back_populates='dessert', cascade="all, delete")

    def __repr__(self):
        return f"Dessert:{self.dessert_name},Price:{self.dessert_price}"


class DeliveryDriver(db.Model):
    db.__tablename__ = 'delivery_driver'
    delivery_driver_id = db.Column(db.Integer, primary_key=True)
    delivery_driver_name = db.Column(db.String(20), nullable=False)
    delivery_driver_area = db.Column(db.Integer, nullable=False)
    order = db.relationship('Order', back_populates='delivery_driver', cascade="all, delete")

    def __repr__(self):
        return f"Delivery driver name{self.delivery_driver_name}, delivered in this area{self.delivery_driver_area}"


order_to_menu_table = db.Table('menu_to_order',
                               db.Column('order_id', db.Integer, db.ForeignKey('order.order_id')),
                               db.Column('menu_id', db.Integer, db.ForeignKey('menu.menu_id')),
                               db.Column('count', db.Integer, default=1))


class Menu(db.Model):
    db.__tablename__ = 'menu'
    menu_id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.pizza_id'))
    drinks_id = db.Column(db.Integer, db.ForeignKey('drinks.drinks_id'))
    dessert_id = db.Column(db.Integer, db.ForeignKey('dessert.dessert_id'))
    order = relationship("Order", back_populates="menu", lazy='dynamic', secondary=order_to_menu_table, cascade="all, delete")
    pizza = relationship("Pizza", back_populates="menu", cascade="all, delete")
    drinks = relationship("Drinks", back_populates="menu", cascade="all, delete")
    dessert = relationship("Dessert", back_populates="menu", cascade="all, delete")



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
    driver_id = db.Column(db.Integer, db.ForeignKey('delivery_driver.delivery_driver_id'))
    customer = db.relationship('Customer', back_populates='order', cascade="all, delete")
    delivery_driver = db.relationship('DeliveryDriver', back_populates='order', cascade="all, delete")
    menu = relationship("Menu", back_populates="order", lazy='dynamic', secondary=order_to_menu_table, cascade="all, delete")

    def __repr__(self):
        return f"Order {self.order_id}, came in at {self.placed}, currently {self.status}, " \
               f"discount applied {self.discount}, entered by {self.customer_id}"



# class Order_Menu(db.Model):
#     db.__tablename__='order_menu'
#     menu_id = db.Column(db.Integer, db.ForeignKey('menu.menu_id'),nullable=False)
#     order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'),nullable=False)
#     order = db.relationship('Order', backref=db.backref('order_menu', lazy=True))
#     menu = db.relationship('Menu', backref=db.backref('order_menu', lazy=True))


db.drop_all()
db.create_all()


from model.fill import *
fillDB()
