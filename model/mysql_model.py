import mysql.connector
import pymysql
from pathlib import Path
from app import app
from flask_sqlalchemy import SQLAlchemy



# DB_NAME = 'Pizza_DKE'
#
# TABLES = {}
#
# TABLES ['customers'] = (
#     "CREATE TABLE `customers`("
#     "   `customer_id` int NOT NULL AUTO_INCREMENT,"
#     "   `first_name` varchar(30) NOT NULL,"
#     "   `last_name` varchar(40) NOT NULL,"
#     "   `email_address` varchar(50) NOT NULL UNIQUE,"
#     "   `address_street` varchar(40) NOT NULL,"
#     "   `address_number` varchar(5) NOT NULL,"
#     "   `address_postal_code` varchar(7) NOT NULL,"
#     "   `address_city` varchar(40) NOT NULL,"
#     "   `active_code` boolean,"
#     "   PRIMARY KEY (`customer_id`)"
#     ")"
# )
#
# TABLES ['order'] = (
#     "CREATE TABLE `order`("
#     "   `order_id` int NOT NULL AUTO_INCREMENT,"
#     "   `status` enum('cancelled', 'in process', 'out for delivery') NOT NULL,"
#     "   `order_placed` datetime NOT NULL, "
#     "   `discount_code` boolean,"
#     "   `customer_id` int NOT NULL,"
#     "   PRIMARY KEY (`order_id`),"
#     "   CONSTRAINT `customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`) ON DELETE SET NULL"
#     ")"
# )
#
# TABLES ['delivery_driver'] = (
#     "CREATE TABLE `delivery_driver` ("
#     "   `driver_id` int NOT NULL AUTO_INCREMENT"
#     "   ``"
#
# )
# Boolean = tinyint (1)


