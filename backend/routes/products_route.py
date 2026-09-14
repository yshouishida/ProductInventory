from flask import Blueprint

from backend.controllers.product_controller import (
    get_products_control,
    get_by_id_control,
    add_product_control,
    update_product_control,
    delete_product_control
)


products_bp = Blueprint("products", __name__)


products_bp.route("/products", methods=["GET"])
def get_products():
    return get_products_control()