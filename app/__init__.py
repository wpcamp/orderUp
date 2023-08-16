from flask import Flask
from .config import Configuration
from .routes import orders
from .models import db   # New import

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(orders.bp)
db.init_app(app)  # Configure the application with SQLAlchem
