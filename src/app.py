from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
# create the flask app
app = Flask(__name__)

# params of connection
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'secret_key'
conex = SQLAlchemy(app)

# Blueprint
from routes.contacts import contact
app.register_blueprint(contact)

#error handling, response status code 404
def default_error(error):
    return '<p>Have you evil inserted the URL? Try again later</p>'
