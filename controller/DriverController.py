from db import db
from model.mysql_model import DeliveryDriver


def save_new_delivery_driver(name, area):
    new_delivery_driver = DeliveryDriver(delivery_driver_name=name, delivery_driver_area = area)
    db.session.add(new_delivery_driver)
    db.session.commit()
    return new_delivery_driver


def find_single_driver(**kwargs):
    return DeliveryDriver.query.filter_by(**kwargs).first()


def get_all_drivers():
    return DeliveryDriver.query.all()

