from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Employee(db.Model, UserMixin):  # Your class definition
    # Mapping attributes, here
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.Integer, nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Menu(db.Model):
    __tablename__ = "menus",
    id = db.Column("id", db.Integer, primary_key=True),
    name = db.Column("name", db.String(30), nullable=False)
    items = db.relationship("menu_items", back_populates="menus")

class MenuItem(db.Model):
    __tablename__ = "menu_items",
    id = db.Column("id", db.Integer, primary_key=True),
    name = db.Column("name", db.String(50), nullable=False),
    price = db.Column("price", db.Float, nullable=False),
    menu_id = db.Column("menu_id", db.Integer,
                        db.ForeignKey("menus.id"), nullable=False),
    menu_type_id = db.Column("menu_type_id", db.Integer, db.ForeignKey(
        "menu_item_types.id"), nullable=False)

    menu = db.relationship("menus", back_populates="menu_item")


class MenuItemTypes(db.Model):
    __tablename__ = "menu_item_types",
    id = db.Column("id", db.Integer, primary_key=True),
    name = db.Column("name", db.String(20), nullable=False)
