import app
from flask import Flask, render_template, request, redirect, session


from flask import Blueprint

# from controllers.UserController import index, store, show, update, destroy

# user_bp = Blueprint('user_bp', __name__)
# user_bp.route('/', methods=['GET'])(index)
# user_bp.route('/create', methods=['POST'])(store)
# user_bp.route('/<int:user_id>', methods=['GET'])(show)
# user_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
# user_bp.route('/<int:user_id>', methods=['DELETE'])(destroy)


@app.route('/', methods=['GET'])
def index():
    # check for customer Email
    # if in  DB - order
    # else customer creation (no customer retention rate)
    # after -> ordering
    # 1) customerSignIn()
    return redirect('/order')

@app.route('/order', methods=['POST'])
def store():
    # call for storing the order in the DB
    # get back the order instance
    # if customer Email is unknown - add customer and request the info
