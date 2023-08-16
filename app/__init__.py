from flask import Flask, Blueprint
from .config import Configuration
from .routes.session import session
from .routes.orders import orders
from .models import db, Employee
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(orders)
app.register_blueprint(session, url_prefix='/session')
db.init_app(app)  # Configure the application with SQLAlchem



login = LoginManager(app)
login.login_view = "session.login"


@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))
