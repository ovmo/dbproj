# import sys
# from flask import render_template, redirect, url_for, request, render_template, request, redirect, session
from db import db
from model.mysql_model import Address, Customer


def find_single_address(**kwargs):
    return Address.query.filter_by(**kwargs).first()


def save_new_address(street, street_no, code, city):
    new_address = Address(street=street, street_no=street_no, code=code, city=city)
    db.session.add(new_address)
    db.session.commit()
    return new_address


def find_single_customer(**kwargs):
    return Customer.query.filter_by(**kwargs).first()


def save_new_costumer(email, street, street_no, code, city):
    new_address = save_new_address(street=street, street_no=street_no, code=code, city=city)
    new_customer = Customer(email=email, address=new_address)
    print(new_customer)
    if new_customer.email != "":
        db.session.add(new_customer)
        db.session.commit()
        return new_customer
    else:
        return AttributeError






