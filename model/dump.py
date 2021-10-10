# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Table, Column, Integer, ForeignKey, null
# from sqlalchemy.ext.declarative import declarative_base


#menu
# pizza = db.relationship('Pizza', backref=db.backref('menu', lazy=True))
    # drinks = db.relationship('Drinks', backref=db.backref('menu', lazy=True))
    # dessert = db.relationship('Dessert', backref=db.backref('menu', lazy=True))

# driver_to_order_table = db.Table('driver_to_order',
#                                  db.Column('order_id', db.Integer, db.ForeignKey('order.order_id'), primary_key=True),
#                                  db.Column('driver_id', db.Integer,
#                                            db.ForeignKey('delivery_driver.delivery_driver_id'),))


# class Order_Delivery(db.Model):
#     db.__tablename__='order_delivery'
#     order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
#     delivery_driver_id = db.Column(db.Integer, db.ForeignKey('delivery_driver.delivery_driver_id'))
#     delivery_driver = db.relationship('delivery_driver', backref=db.backref('order_delivery', lazy=True))
#     order = db.relationship('order', backref=db.backref('order_delivery', lazy=True))
#
#
# def save_new_pizza(name, toppings):
#     new_pizza = Pizza(name=name)
#     db.session.add(new_pizza)
#     for i in range(1, len(toppings)):
#         # topping = find_single_topping(toppings.toppings_name)
#         topping = find_single_topping(name=toppings[i])
#         if topping is None:
#             return Exception(DatabaseError)
#         # new_pizza_topping = Pizza_Toppings(pizza_id=new_pizza.id, toppings_id=topping.id)
#         # db.session.add(new_pizza_topping)
#         db.session.commit()
#         # create topping Pizza link
#
#     new_menu_item = Menu(pizza_id=new_pizza.id)
#     db.session.add(new_menu_item)
#     db.session.commit()
#     return new_pizza



# class Pizza_Toppings(db.Model):
#     db.__tablename__='pizza_toppings'
#     pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.pizza_id'), nullable=False)
#     toppings_id = db.Column(db.Integer, db.ForeignKey('toppings.toppings_id'), nullable=False)
#

