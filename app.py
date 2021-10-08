from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DatabaseError
from db import app
# import sqlalchemy
from controller.CustomerController import find_single_customer, save_new_costumer
from controller.FormCustomer import CustomerCreation
from controller.FormOrdering import OrderCreation
from controller.OrderController import save_new_order, find_single_order
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
    form = OrderCreation('/order')
    if request.method == 'POST':
        menu = request.form['pizzas'] + request.form['drinks'] + request.form['dessert']
        customer = find_single_customer(email=request.form['email'])
        new_order = save_new_order(email=request.form['email'],
                                   menu=menu,
                                   discount=customer.codeActive)
        return redirect('/order/<int:new_order.order_id>')
    return render_template("order.html", form=form, title="Order")


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
    form = CustomerCreation("/customer")
    if request.method == "POST":
        customer_found = save_new_costumer(email=request.form['email'],
                                           street=request.form['street'],
                                           street_no=request.form['street_no'],
                                           code=request.form['postal_code'],
                                           city=request.form['city'])
        return redirect('/order')
    else:

        return render_template("CreateCustomer.html", form=form)


@app.route('/customer/<int:customer_id>', methods=['GET'])
def customer_id(customer_id):
    if request.method == 'GET':
        customer_found = find_single_customer(customer_id=customer_id)
        if customer_found is None:
            return redirect(special_exception_handler(Exception))
        else:
            return render_template('CustomerID.html', customer=customer_found)
    else:
        # 404
        return redirect(page_not_found(PermissionError))



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
