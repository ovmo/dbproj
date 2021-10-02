
from pathlib import Path
from app import *
from app import db
import enum
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Path("db").mkdir(parents=True, exist_ok=True)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:otto@localhost:3306"


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


def find_single_address(**kwargs):
    return Address.query.filter_by(**kwargs).first()

def save_new_address(street, street_no, code, city):
    new_address = Address(street=street, street_no=street_no, code=code, city=city)
    db.session.add(new_address)
    db.session.commit()
    return new_address


class Customer(db.Model):
    db.__tablename__ = 'customer'
    customer_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.address_id'), nullable=False)
    codeActive = db.Column(db.Boolean)
    address = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User {self.email}"


def find_single_customer(**kwargs):
    return Customer.query.filter_by(**kwargs).first()


def save_new_costumer(email, street, street_no, code, city):
    new_address = save_new_address(street, street_no, code, city)
    new_customer = Customer(email=email, address_id=new_address.address_id)

    if new_customer.email != "":
        db.session.add(new_customer)
        db.session.commit()
        return new_customer
    else:
        return AttributeError


class Pizza(db.Model):
    db.__tablename__ = 'pizza'
    pizza_id = db.Column(db.Integer, primary_key= True)
    pizza_name = db.Column(db.String(40),nullable = False)
    toppings = relationship("Topping", back_populates="pizza")

    def __repr__(self):
        return f"Pizza {self.pizza_name}, Toppings: {self.toppings}"


def save_new_pizza(name, toppings):
    new_pizza = Pizza(name=name)
    db.session.add(new_pizza)
    for i in range(1, len(toppings)):
        # topping = find_single_topping(toppings.toppings_name)
        topping = find_single_topping(toppings[i])
        new_pizza_topping = Pizza_Toppings(pizza_id=new_pizza.id, toppings_id=topping.id)
        db.session.add(new_pizza_topping)
    new_menu_item = Menu(pizza_id=new_pizza.id)
    db.session.add(new_menu_item)
    db.session.commit()
    return new_pizza


def find_single_pizza(**kwargs):
    return Pizza.query.filter_by(**kwargs).first()


class Pizza_Toppings(db.Model):
    db.__tablename__='pizza_toppings'
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.pizza_id'), nullable=False)
    toppings_id = db.Column(db.Integer, db.ForeignKey('toppings.toppings_id'), nullable=False)


class Toppings(db.Model):
    db.__tablename__ = 'toppings'
    toppings_id = db.Column(db.Integer, primary_key=True)
    toppings_name = db.Column(db.String(40),nullable=False)
    toppings_price = db.Column(db.Integer, nullable=False)
    toppings_vegi = db.Column(db.Boolean)
    pizza = relationship("Pizza", back_populates="toppings", secondary=Pizza_Toppings)

    def __repr__(self):
        return f"Toppings:{self.toppings_name}, Price:{self.toppings_price}, Vegi?{self.toppings_vegi}"


def save_new_toppings(name, price, vegi):
    new_toppings = Toppings(toppings_name=name, toppings_price=price, toppings_vegi=vegi)
    db.session.add(new_toppings)
    db.session.commit()
    return new_toppings


def find_single_topping(**kwargs):
    return Toppings.query.filter_by(**kwargs).first()


class Drinks(db.Model):
    db.__tablename__='drinks'
    drinks_id = db.Column(db.Integer, primary_key=True)
    drinks_name = db.Column(db.String(40), nullable=False)
    drinks_price = db.Column( db.Integer, nullable=False)

    def __repr__(self):
        return f"Drinks:{self.drinks_name},Price:{self.drinks_price}"


def save_new_drinks(name,price):
    new_drinks = Drinks(drinks_name= name,drinks_price=price)
    new_menu_item = Menu(drinks_id=new_drinks.id)
    db.session.add(new_menu_item)
    db.session.add(new_drinks)
    db.session.commit()
    return new_drinks


def find_single_drinks(**kwargs):
    return Drinks.query.filter_by(**kwargs).first()


class Dessert(db.Model):
    db.__tablename__='dessert'
    dessert_id = db.Column(db.Integer, primary_key=True)
    dessert_name = db.Column(db.String(40), nullable=False)
    dessert_price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Dessert:{self.dessert_name},Price:{self.dessert_price}"


def save_new_desserts(name,price):
    new_desserts = Dessert(dessert_name=name, dessert_price=price)
    new_menu_item = Menu(dessert_id=new_desserts.id)
    db.session.add(new_menu_item)
    db.session.add(new_desserts)
    db.session.commit()
    return new_desserts


def find_single_dessert(**kwargs):
    return Dessert.query.filter_by(**kwargs).first()


class Delivery_Driver(db.Model):
    db.__tablename__='delivery_driver'
    delivery_driver_id = db.Column(db.Integer, primary_key=True)
    delivery_driver_name = db.Column(db.String(20), nullable=False)
    delivery_driver_area = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Delivery driver name{self.delivery_driver_name}, delivered in this area{self.delivery_driver_area}"


def save_new_delivery_driver(name,area):
    new_delivery_driver = Delivery_Driver(delivery_driver_name=name, delivery_driver_area = area)
    db.session.add(new_delivery_driver)
    db.session.commit()
    return new_delivery_driver


def find_single_driver(**kwargs):
    return Delivery_Driver.query.filter_by(**kwargs).first()


class Order_Delivery(db.Model):
    db.__tablename__='order_delivery'
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    delivery_driver_id = db.Column(db.Integer, db.ForeignKey('delivery_driver.delivery_driver_id'))


class Menu(db.Model):
    db.__tablename__='menu'
    menu_id = db.Column(db.Integer,primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.pizza_id'),nullable=False)
    drinks_id = db.Column(db.Integer, db.ForeignKey('drinks.drinks_id'),nullable=False)
    dessert_id = db.Column(db.Integer, db.ForeignKey('dessert.dessert_id'),nullable=False)


def find_single_menu(**kwargs):
    return Menu.query.filter_by(**kwargs).first()

class OrderEnum(enum.Enum):
    out_for_delivery = 1
    in_process = 2
    canceled = 3


class Order (db.Model):
    db.__tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(OrderEnum), nullable=False)
    placed = db.Column(db.DateTime, nullable=False)
    discount = db.Column(db.Boolean)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)

    def __repr__(self):
        return f"Order {self.order_id}, came in at {self.placed}, currently {self.status}, " \
               f"discount applied {self.discount}, entered by {self.customer_id}"


def find_single_order(**kwargs):
    return Order.query.filter_by(**kwargs).first()


def save_new_order(email, menu, discount):
    customer = find_single_customer(email)
    new_order = Order(email=email, discount=discount, customer_id=customer.id, placed=datetime.datetime.now())
    db.session.add(new_order)
    for i in range(1,len(menu)):
        menu_item = find_single_menu(menu[i])
        new_order_menu = Order_Menu(order_id=new_order.id, menu_id=menu_item.id)
        db.session.add(new_order_menu)
    db.session.commit()
    return new_order


class Order_Menu(db.Model):
    db.__tablename__='order_menu'
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.menu_id'),nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'),nullable=False)


db.create_all()
