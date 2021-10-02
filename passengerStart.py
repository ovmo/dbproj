from flask import Flask
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

application = Flask(__name__)
csrf.init_app(application)

application.config.from_object('config')

import model.mysql_model
from controller import *

if __name__ == '__main__':
    application.run(port=8000)

