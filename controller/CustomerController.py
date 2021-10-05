import sys
from flask import render_template, redirect, url_for, request, abortFlask, render_template, request, redirect, session
from app import *
import model.mysql_model
from model.mysql_model import *
from manage import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@app.route('/customer', methods=['POST'])
def customer():

    customer = save_new_costumer(email = request.form['email'],
                                 street = request.form['street'],
                                 street_no = request.form['street_no'],
                                 code = request.form['postal_code'],
                                 city = request.form['city']
                                 )
    return redirect('/')

@app.route('/customer/<int:customer_id>', methods=['GET'])
def customer_id(customer_id):
    session = Session()
    if request.method == 'GET':
        customer = find_single_customer(customer_id=customer_id)

        return render_template('CustomerID.html', customer=customer)
    else:
        return redirect(page_not_found(DatabaseError))
        #404


