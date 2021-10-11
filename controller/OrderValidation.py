from flask import render_template, redirect
from sqlalchemy import exists
from app import db
from controller.CustomerController import customer_id, customer
from controller.FormCustomer import CustomerCreation
from model.mysql_model import *
from model.fill import *
import timeit


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
def pizzaExist():

    p = db.session.query(exists(menu.pizza_id).where()).scalar()
    return p



def addDriver():
    code1 = address.code

    area = int(str(code1)[:3])

    if area == delivery_driver.delivery_driver_area:
        driver1= Delivery_driver(Somename, area) # find a way to select a driver which is in the area, we don't care about the name
        db.session.add(driver1)
        db.session.commit()
        #find a way to see if a driver is available ? Timing system?
        # maybe use the OrderEnum class for the state of the order

        start = timeit.timeit()
        #add action to driver a calculate if the driver is available
        end = timeit.timeit()
        print(end - start) # total time taken

    else:
        #continue looking for another driver





def Orderdetails():
    driver_name = delivery_driver.delivery_driver_name
    order_id = order.order_id
    return 'Delivery driver name '+ driver_name + ', your order number is ' +order_id





