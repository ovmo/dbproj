from flask import render_template, redirect
from sqlalchemy import exists
from app import db
from controller.CustomerController import customer_id, customer
from controller.FormCustomer import CustomerCreation
from model.mysql_model import *
from model.fill import *
import timeit
from controller.DriverController import *


def check_customer_exist():
    c = db.session.query(exists().where(customer.id == customer_id)).scalar()
    if c:
        return redirect('/')
    else:
        return render_template("CreateCustomer.html", form=CustomerCreation)


# check if they have a pizza in order
def pizza_exist():
    p = db.session.query(exists(menu.pizza_id).where(pizza.id == pizza_id)).scalar()
    return p


def need_driver():
    drivers = get_all_drivers
    for delivery_driver in drivers:
        timenow = datetime.utcnow()
        orderplaced = delivery_driver.orders[-1].placed
        f = (orderplaced - timenow).seconds/60
        drivers[i] = find_single_driver(delivery_driver.delivery_driver_area)
        if (drivers[i] == delivery_driver.area) & (f >= 35):
            return drivers[i]


def orderdetails():
    driver_name = delivery_driver.delivery_driver_name
    order_id = order.order_id
    return 'Delivery driver name ' + driver_name + ', your order number is ' + order_id
