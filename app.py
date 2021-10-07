from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DatabaseError
from flask_migrate import Migrate


# from models.User import db
# from routes.user_bp import user_bp
import sqlalchemy

#from model.mysql_model import *
import routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:otto@localhost:3306/dbproj"
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    # check for customer Email
    # if in  DB - order
    # else customer creation (no customer retention rate)
    # after -> ordering
    # 1) customerSignIn()
    return render_template("index.html")


@app.route('/order', methods=['POST'])
def store():
    # call for storing the order in the DB
    # get back the order instance
    # if customer Email is unknown - add customer and request the info
    print("")


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.errorhandler(DatabaseError)
def special_exception_handler(error):
    return 'Database connection failed', 500


db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, use_debugger=False, use_reloader=False)
    app.run()
