from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DatabaseError
from db import app
# import sqlalchemy
from controller.CustomerController import find_single_customer, save_new_costumer
from controller.FormCustomer import CustomerCreation
from controller.FormOrdering import OrderCreation
from controller.ControllerMenu import get_all_pizzas, get_all_drinks, get_all_desserts, find_single_menu
from controller.OrderController import save_new_order, find_single_order, orderProcessing


# from model.mysql_model import Address, Customer, DeliveryDriver, Pizza, Toppings,
# Drinks, Dessert, Menu, OrderEnum, Order


@app.route('/', methods=['GET'])
def index():
    # check for customer Email
    # if in  DB - order
    # else customer creation (no customer retention rate)
    # after -> ordering
    # 1) customerSignIn()
    return render_template("index.html")


# Ordering routes
@app.route('/order', methods=['POST', 'GET'])
def route_ordering():
    if request.method == 'POST':
        orderProcessing(request.form)
        # menu = []
        # form =
        # for i in range(len(form)):
        #     if i != 1:
        #         if form[i][1] != 0:
        #             menu.append(find_single_menu())
        # customer = find_single_customer(email=form['email'])
        # new_order = save_new_order(email=form['email'],
        #                            menu=menu,
        #                            discount=customer.codeActive)
        # return redirect('/order/<int:new_order.order_id>')
    pizzas = get_all_pizzas()
    pizzaPrices = []
    for pizza in pizzas:
        pizzaPrice = 0
        for topping in pizza.toppings:
            pizzaPrice += topping.toppings_price
        pizzaPrices.append((pizzaPrice/0.6) * 1.09)
    drinks = get_all_drinks()
    desserts = get_all_desserts()
    return render_template("order.html", pizzaMenu=pizzas, drinksMenu=drinks, dessertMenu=desserts, pizzaMenuPrices=pizzaPrices, title="Order")


@app.route('/order/<order_id>', methods=['GET'])
def route_order_id(order_id):
    if request.method == 'GET':
        order = find_single_order(order_id=order_id)
        if order is None:
            return redirect(special_exception_handler(Exception))
        else:
            return render_template('order_id.html', order=order, title="Order")
    else:
        return redirect(page_not_found(Exception))
        #404


@app.route('/customer', methods=['GET', 'POST'])
def customer():
    print(request)
    if request.method == "POST":
        print(request.form)
        new_customer = save_new_costumer(email=request.form['email'],
                                         street=request.form['street'],
                                         street_no=request.form['street_no'],
                                         code=request.form['postal_code'],
                                         city=request.form['city'])
        return redirect('/order')
    else:
        return render_template("CreateCustomer.html")


# @app.route('/customer/<int:customer_id>', methods=['GET'])
# def customer_id(customer_id):
#     if request.method == 'GET':
#         customer_found = find_single_customer(customer_id=customer_id)
#         if customer_found is None:
#             return redirect(special_exception_handler(Exception))
#         else:
#             return render_template('CustomerID.html', customer=customer_found)
#     else:
#         # 404
#         return redirect(page_not_found(PermissionError))


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.errorhandler(DatabaseError)
def special_exception_handler(error):
    return 'Database connection failed', 500


@app.errorhandler(AttributeError)
def pizza_missing(error):
    return "Please order a Pizza so we can get the order on the way", 404


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, use_debugger=False, use_reloader=False)
    app.run()
