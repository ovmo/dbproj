import sys
from flask import render_template, redirect, url_for, request, abortFlask, render_template, request, redirect, session
from app import *
import model.mysql_model
from model.mysql_model import *
from FormOrdering import OrderCreation
from manage import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@app.route('/order', methods=['POST'])
def route_ordering():
    if request.method == 'POST':
        menu = request.form['pizzas'] + request.form['drinks'] + request.form['dessert']
        customer = find_single_customer(email=request.form['email'])
        new_order = save_new_order(email=request.form['email'],
                                   menu=menu,
                                   discount=customer.codeActive
                                   )
        return redirect('/order/<int:new_order.order_id>')
    else:
        render_template("order.html", form=OrderCreation, title="Order")


@app.route('/order/<order_id>', methods=['GET'])
def route_order_id(order_id):
    if request.method == 'GET':
        order = find_single_order(order_id=order_id)
        if order is None:
            return redirect(page_not_found(DatabaseError))
        else:
            return render_template('order_id.html', order=order, title="Order")
    else:
        return redirect(page_not_found(PermissionError))
        #404

# def store():
# def show(customerID):
# def update(customerID):

