# import sys
from datetime import datetime

from flask import render_template, redirect, url_for, request, render_template, request, redirect, session
# from app import page_not_found, pizza_missing, db
# from FormOrdering import OrderCreation
# from flask_sqlalchemy import SQLAlchemy
# from ControllerMenu import find_single_menu
from controller.ControllerMenu import find_single_menu
from controller.CustomerController import find_single_customer
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
        for i in range(1, len(menu)):
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
            new_order = Order(email=email, discount=discount, customer_id=customer.id, placed=datetime.utcnow, menu=order_menu)
            db.session.add(new_order)
            db.session.commit()
            return new_order
        else:
            return pizza_missing(Exception)



