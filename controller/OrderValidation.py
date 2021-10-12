from datetime import datetime

from flask import render_template, redirect
from sqlalchemy import exists
from db import db
from controller.FormCustomer import CustomerCreation
from model.mysql_model import Menu, Pizza, Customer
from controller.DriverController import get_all_drivers


def check_customer_exist(customer_id):
    c = db.session.query(exists().where(Customer.customer_id == customer_id)).scalar()
    if c:
        return redirect('/')
    else:
        return render_template("CreateCustomer.html", form=CustomerCreation)


# check if they have a pizza in order
def pizza_exist(pizza_id):
    p = db.session.query(exists(Menu.pizza_id).where(Pizza.pizza_id == pizza_id)).scalar()
    return p


def need_driver(area):
    area = int(str(area)[:3])

    drivers = get_all_drivers()
    # print("got all drivers")
    for delivery_driver in drivers:
        # print("Checking availablility of drivers")
        if area == delivery_driver.delivery_driver_area:
            # print("getting the driver")
            orders = delivery_driver.order
            if len(orders) < 1:
                return delivery_driver
            timenow = datetime.utcnow()
            # print("time")
            orderplaced = orders[-1].placed
            # print("orderPlaced")
            difference = (timenow - orderplaced).seconds / 60
            # print("differernce")
            if difference >= 35:
                # print("getting driver" + delivery_driver.delivery_driver_name)
                return delivery_driver
    print("emergency driver")
    return drivers[-1]

# def orderdetails():
#     driver_name = delivery_driver.delivery_driver_name
#     order_id = order.order_id
#     return 'Delivery driver name ' + driver_name + ', your order number is ' + order_id
