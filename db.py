from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:otto@localhost:3306/dbproj"
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'dbProject'
db.init_app(app)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources
# engine = create_engine('SQLALCHEMY_DATABASE_URI')

# Session = sessionmaker(engine)
#
# db.session = Session()


