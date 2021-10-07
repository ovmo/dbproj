import sys
from flask import render_template, redirect, url_for, request, abortFlask, render_template, request, redirect, session
from app import *
import model.mysql_model
from model.mysql_model import *
from FormCustomer import CustomerCreation
from manage import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == "POST":
        customer = save_new_costumer(email = request.form['email'],
                                     street = request.form['street'],
                                     street_no = request.form['street_no'],
                                     code = request.form['postal_code'],
                                     city = request.form['city']
                                     )
        return redirect('/order')
    else:

        return render_template("CreateCustomer.html", form=CustomerCreation)

@app.route('/customer/<int:customer_id>', methods=['GET'])
def customer_id(customer_id):
    if request.method == 'GET':
        customerFound = find_single_customer(customer_id=customer_id)
        if customerFound is None:
            return redirect(page_not_found(DatabaseError))
        else:
            return render_template('CustomerID.html', customer=customerFound)
    else:
        return redirect(page_not_found(PermissionError))
        #404


