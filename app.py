from flask import Flask, render_template
from sqlalchemy.exc import DatabaseError

from model.mysql_model import *
import routes

app = Flask(__name__)
db = SQLAlchemy(app)

# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.errorhandler(DatabaseError)
def special_exception_handler(error):
    return 'Database connection failed', 500

if __name__ == '__main__':
    app.run()




from flask_migrate import Migrate
from models.User import db
from routes.user_bp import user_bp
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(user_bp, url_prefix='/users')
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.debug = True
    app.run()