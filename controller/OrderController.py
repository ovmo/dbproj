# import sys
from datetime import datetime

from flask import render_template, redirect, url_for, request, render_template, request, redirect, session
# from app import page_not_found, pizza_missing, db
# from FormOrdering import OrderCreation
# from flask_sqlalchemy import SQLAlchemy
# from ControllerMenu import find_single_menu
from controller.ControllerMenu import find_single_menu
from controller.CustomerController import find_single_customer
from db import db
from model.mysql_model import Order


def find_single_order(**kwargs):
    return Order.query.filter_by(**kwargs).first()


def save_new_order(email, menu, discount):
    customer = find_single_customer(email=email)
    if customer is None:
        return redirect('/customer.html')
    else:
        order_menu = []
        pizza_ordered = False
        for i in range(0, len(menu)):
            menu_item = find_single_menu(menu_id=menu[i])
            if menu_item is None:
                return f"{menu[i]} Item not in the Menu"
                # return page_not_found(Exception)
            else:
                if menu_item.pizza is not None:
                    pizza_ordered = True
                order_menu.append(menu_item)
            # new_order_menu = Order_Menu(order_id=new_order.id, menu_id=menu_item.id)
            # db.session.add(new_order_menu)
        if pizza_ordered:
            new_order = Order(email=email, discount=discount, customer=customer, placed=datetime.utcnow, menu=order_menu)
            db.session.add(new_order)
            db.session.commit()
            return new_order
        else:
            return "Pizza Missing from the order"


def orderProcessing(form):
    menu = []
    print(form)
    # if form.get("1") != 0:
    #     find_single_menu(menu_id=1)
    pizzaOrdered = False
    customer = find_single_customer(email=form.get('email'))
    print('email ' + form.get('email'))
    print('cust ')
    print(customer)
    discount = False
    if customer is None:
        print("redirect Customer Creation - no customer found ")
        # return redirect('/customer')
        # return render_template('CreateCustomer.html', message='Please create an account first.')
    # else:
        # discount = check_discount(customer)

    print('10%' + str(discount))
    for item in form.items():
        if is_integer(item[1]) and int(item[1]) > 0:
            menuItem = find_single_menu(menu_id=item[0])
            menu.append(menuItem)
            if int(item[0]) <= 14:
                pizzaOrdered = True

    if pizzaOrdered:
        print("pizza in onrder " + str(pizzaOrdered))
    print(menu)
    print(datetime.utcnow())
    new_order = Order(discount=discount, customer_id=customer.customer_id, placed=datetime.utcnow, menu=menu, status='in_process')
    # new_order = Order(discount=discount, customer_id=customer.customer_id,
    # placed=datetime.utcnow, menu=menu, status='in_process', customer=customer)
    print(new_order)
    db.session.add(new_order)
    db.session.commit()
    return new_order
    # else:
    #     return render_template('order.html', message="Please order a pizza so we can prepare the order for you...")


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def check_discount(customer):
    all_orders = customer.orders
    count_pizza = 0
    for order in all_orders:
        if order.discount:
            count_pizza = 0
        else:
            for menuItem in order.menu:
                if menuItem.menu_id <= 14:
                    count_pizza += 1
    if count_pizza >= 10:
        return True
    else:
        return False
