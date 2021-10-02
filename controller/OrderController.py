import sys
from flask import render_template, redirect, url_for, request, abortFlask, render_template, request, redirect, session
from app import *
import model.mysql_model
from model.mysql_model import *
from manage import *
from config import Session
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


@app.route('/order', methods=['POST'])
def route_ordering():
    session = Session()
    menu = request.form['pizzas'] + request.form['drinks'] + request.form['dessert']
    customer = find_single_customer(email=request.form['email'])
    new_order = save_new_order(email = request.form['email'],
                               menu = menu,
                               discount=customer.codeActive
                               )
    return redirect('/order/<int:new_order.order_id>', )



@app.route('/order/<order_id>', methods=['GET'])
def route_order_id(order_id):
    session = Session()
    if request.method == 'GET':
        order = find_single_order(order_id=order_id)
        return render_template('order_id.html', order=order)
    else:
        return redirect(page_not_found(DatabaseError))
        #404




# def store():
# def show(customerID):
# def update(customerID):

