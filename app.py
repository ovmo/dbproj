import datetime
from datetime import datetime

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DatabaseError
from db import app, db
# import sqlalchemy
from controller.CustomerController import find_single_customer, save_new_costumer
from controller.FormCustomer import CustomerCreation
from controller.FormOrdering import OrderCreation
from controller.ControllerMenu import get_all_pizzas, get_all_drinks, get_all_desserts, find_single_menu, \
    find_single_pizza
from controller.OrderController import save_new_order, find_single_order, orderProcessing


# from model.mysql_model import Address, Customer, DeliveryDriver, Pizza, Toppings,
# Drinks, Dessert, Menu, OrderEnum, Order
from model.mysql_model import order_to_menu_table, OrderEnum


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
    if request.method == 'GET':
        pizzas = get_all_pizzas()
        pizzaPrices = []
        # pizzaVegis = []
        for pizza in pizzas:
            pizzaPrice = 0
            # pizzaVegi = True
            for topping in pizza.toppings:
                # if not topping.vegi:
                    # pizzaVegi = False
                pizzaPrice += topping.toppings_price
            # pizzaVegis.append(pizzaVegi)
            pizzaPrices.append((pizzaPrice / 0.6) * 1.09)
        drinks = get_all_drinks()
        desserts = get_all_desserts()
        # return render_template("order.html", pizzaMenu=pizzas, drinksMenu=drinks, dessertMenu=desserts,
        #                        pizzaMenuPrices=pizzaPrices, pizzaMenuVegi=pizzaVegis, title="Order")
        return render_template("order.html", pizzaMenu=pizzas, drinksMenu=drinks, dessertMenu=desserts,
                               pizzaMenuPrices=pizzaPrices, title="Order")
    if request.method == 'POST':
        order = orderProcessing(request.form)
        print(order)
        if order is not None:
            print("going to order ID")
            print(order.order_id)
            # return order
            return route_order_id(order.order_id)
            # return redirect(f"/order/{order.order_id}")
        else:
            return redirect("/order")


@app.route('/order/<int:order_id>', methods=["POST", "GET"])
def route_order_id(order_id):
    print("Order ID Entered")
    order = find_single_order(order_id=order_id)
    if order is not None:
        status = ""
        # order_menu = db.session.query(order_to_menu_table).filter_by(order_id=order.order_id).all()
        difference = (datetime.utcnow() - order.placed).seconds / 60
        if order.status == 'in_process' and difference >= 5:
            order.status = OrderEnum.out_for_delivery
            db.session.commit()
        if order.status == OrderEnum.in_process:
            status = "in Process"
        elif order.status == OrderEnum.out_for_delivery:
            status = 'out for Delivery'
        else:
            status = 'canceled'

        menu = order.menu
        totalPrice = 0
        pizzaPrices = {}
        for item in menu:
            print(item.menu_id)
            if item.menu_id <= 14:
                # print(item.menu_id)
                pizza = find_single_pizza(pizza_id=item.pizza_id)
                pizzaPrice = 0
                for topping in pizza.toppings:
                    pizzaPrice += topping.toppings_price
                pizzaPrices.update({item.menu_id:(pizzaPrice / 0.6) * 1.09})
                # totalPrice += pizzaPrice
            # elif 14 < item.menu_id < 23:
            #     totalPrice += item.drinks_price
            # elif item.menu_id >= 23:
            #     totalPrice += item.dessert_price

        print(menu)
        print(order)
        print(pizzaPrices)
        print(customer)
        return render_template("order_id.html", order=order, menu=menu, pizzaPrices=pizzaPrices, total=totalPrice,
                               customer=order.customer, driver=order.delivery_driver, status=status,
                               title=f"Order {order.order_id}")
        # return render_template("order_id.html", order=order, menu=menu, pizzaPrices=pizzaPrices,
        #                        orderCount=order_menu, customer=order.customer)

    else:
        return redirect("/order", 404)


@app.route('/order/<int:order_id>/cancel', methods=["GET"])
def route_cancel(order_id):
    order = find_single_order(order_id=order_id)
    difference = (datetime.utcnow() - order.placed).seconds / 60
    if difference <= 5:
        order.status = OrderEnum.canceled
        db.session.commit()
    return redirect('/order/<order_id>')


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
        return render_template("CreateCustomer.html", title="Sign Up")


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
