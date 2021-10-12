# import sys
from datetime import datetime
from controller.OrderValidation import need_driver
from flask import render_template, redirect, url_for, request, render_template, request, redirect, session

from controller.ControllerMenu import find_single_menu
from controller.CustomerController import find_single_customer
from db import db
from model.mysql_model import Order#, order_to_menu_table # , OrderToMenu


def find_single_order(**kwargs):
    return Order.query.filter_by(**kwargs).first()


def get_all_orders():
    return Order.query.all()


def save_new_order(email, menu, discount):
    customer = find_single_customer(email=email)
    if customer is None:
        return redirect('/customer.html')
    else:
        order_menu = []
        pizza_ordered = False
        for i in range(0, len(menu)):
            menu_item = find_single_menu(menu_id=menu[i])
            if menu_item is None:
                return f"{menu[i]} Item not in the Menu"
                # return page_not_found(Exception)
            else:
                if menu_item.pizza is not None:
                    pizza_ordered = True
                order_menu.append(menu_item)
            # new_order_menu = Order_Menu(order_id=new_order.id, menu_id=menu_item.id)
            # db.session.add(new_order_menu)
        if pizza_ordered:
            new_order = Order(email=email, discount=discount, customer=customer, placed=datetime.utcnow,
                              menu=order_menu)
            db.session.add(new_order)
            db.session.commit()
            return new_order
        else:
            return "Pizza Missing from the order"


# def save_new_order_to_menu(menu, count, order):
#     new_order_to_menu = OrderToMenu(menu=menu, order=order, count=count)
#     db.session.add(new_order_to_menu)
#     db.session.commit()
#     return new_order_to_menu


def orderProcessing(form):
    menu = []
    print(form)
    # if form.get("1") != 0:
    #     find_single_menu(menu_id=1)
    pizzaOrdered = False
    customer = find_single_customer(email=form.get('email'))
    print('email ' + form.get('email'))
    print('cust ')
    print(customer)
    discount = False
    if customer is None:
        print("redirect Customer Creation - no customer found ")
        return redirect('/customer')
        # return render_template('CreateCustomer.html', message='Please create an account first.')
    # else:
    # discount = check_discount(customer)

    print('10% ' + str(discount))
    for item in form.items():
        if is_integer(item[1]) and int(item[1]) > 0:
            menuItem = find_single_menu(menu_id=item[0])
            menu.append(menuItem)
            if int(item[0]) <= 14:
                pizzaOrdered = True

    if pizzaOrdered:
        print("pizza in onrder " + str(pizzaOrdered))
        print(menu)
        print(datetime.utcnow())
        driver = need_driver(customer.address.code)
        print("driver " + str(driver))
        new_order = Order(discount=discount, customer_id=customer.customer_id, placed=datetime.utcnow(),
                          status='in_process', delivery_driver=driver, driver_id=driver.delivery_driver_id,
                          customer=customer, menu=menu)
        # new_order = Order(discount=discount, customer_id=customer.customer_id,
        # placed=datetime.utcnow, menu=menu, status='in_process', customer=customer)
        print(new_order)
        db.session.add(new_order)
        db.session.commit()
        print("COMMITTED")
        order = get_all_orders()[-1]
        print(order)
        for item in form.items():
            if is_integer(item[1]) and int(item[1]) > 0:
                # print(item[1])
                menuItem = find_single_menu(menu_id=item[0])
                # itemMenu = save_new_order_to_menu(menuItem, int(item[1]), order)
                # query = f"UPDATE menu_to_order SET count={int(item[1])} WHERE menu_to_order.order_id={order.order_id}, " \
                #         f"menu_to_order.menu_id={int(item[0])}"
                # db.session.execute(query)

                # db.session.query(order_to_menu_table).filter(order_to_menu_table.order_id == order.order_id,
                #                                              order_to_menu_table.menu_id == int(item[0])). \
                #     update(dict(count=int(item[1])))

                # db.session(update(order_to_menu_table).where(order_to_menu_table.order_id == order.order_id,
                #                                              order_to_menu_table.menu_id == int(item[0]))

                # for food in db.session.query(order_to_menu_table).all():
                #     if food.order_id == order.order_id and food.menu_id == int(item[0]):
                #         print("updating " + str(order.order_id) + " " + str(int(item[0])) + " count " + str(int(item[0])))
                #         print("food count")
                #         print(food.count)
                #         print(is_integer(item[1]))
                #         print(int(item[2]))
                #         food.count = int(item[1])
                #         print(food.count)
                menu.append(menuItem)
                # menu.append(itemMenu)
                db.session.commit()
                # print("updated")
                db.session.commit()
        return new_order
    # else:
    #     return render_template('order.html', message="Please order a pizza so we can prepare the order for you...")


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def check_discount(customer):
    all_orders = customer.orders
    count_pizza = 0
    for order in all_orders:
        if order.discount:
            count_pizza = 0
        else:
            for menuItem in order.menu:
                if menuItem.menu_id <= 14:
                    count_pizza += 1
    if count_pizza >= 10:
        return True
    else:
        return False
