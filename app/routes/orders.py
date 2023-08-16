from flask import Blueprint

orders = Blueprint("orders", __name__, url_prefix="")


@orders.route("/")
def index():
    return "Order Up!"

