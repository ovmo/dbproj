from flask import render_template, redirect
from sqlalchemy import exists
from app import db
from controller.CustomerController import customer_id, customer
from controller.FormCustomer import CustomerCreation
from model.mysql_model import *
from model.fill import *
import timeit
from controller.DriverController import *



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
    driver1 = find_single_driver(delivery_driver.delivery_driver_area)
    if area == driver1:
        #add driver 1 to a order
        db.session.add(driver1)
        db.session.commit()



        #find a way to see if a driver is available ? Timing system?
        #Maybe : start the time counting when a driver is found. Then calculate the time and when th time is at 35 minutes, the driver is free again
        #start = timeit.timeit()
        #end = timeit.timeit()
        #print(end - start) # total time taken

    else:
        #continue looking for another driver





def Orderdetails():
    driver_name = delivery_driver.delivery_driver_name
    order_id = order.order_id
    return 'Delivery driver name '+ driver_name + ', your order number is ' +order_id







