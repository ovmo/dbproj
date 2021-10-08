from app import db
from model.mysql_model import Delivery_Driver


def save_new_delivery_driver(name,area):
    new_delivery_driver = Delivery_Driver(delivery_driver_name=name, delivery_driver_area = area)
    db.session.add(new_delivery_driver)
    db.session.commit()
    return new_delivery_driver


def find_single_driver(**kwargs):
    return Delivery_Driver.query.filter_by(**kwargs).first()


