from flask import render_template, redirect
from sqlalchemy import exists
from app import db
from controller.CustomerController import customer_id, customer
from controller.FormCustomer import CustomerCreation
from model.mysql_model import *



# q = session.query(Customer.id).filter(Customer.email==email)
# #session.query(q.exists()).scalar()    # returns True or False

#check if the customer exist in the database
def checkCustomerExist():
    c = db.session.query(exists().where(customer.id == customer_id)).scalar()
    if c:
        return redirect('/')
    else:
        return render_template("CreateCustomer.html", form=CustomerCreation)

# check if they have a pizza in order
#def pizzaExist():
#  p = db.session.query(exists().where(in hte order there is a pizza)).scalar()
#  if p:
#     return redirect('/')
#else:
#   return redirect('/order')

# A) add Driver
#driver =...
#driver only exists in the model, do we have to create
# B) add to DB

#db.session.add(driver)
#db.session.commit()

# show their order and Details connected (Order, Delivery Time, final Price, delivery  driver name/id)
