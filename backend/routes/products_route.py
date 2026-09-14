from flask import Blueprint

from backend.controllers.product_controller import (
    get_products_control,
    get_by_id_control,
    add_product_control,
    update_product_control,
    delete_product_control
)


products_bp = Blueprint("products", __name__)


@products_bp.route("/products", methods=["GET"])
def get_products():
    return get_products_control()

@products_bp.route("/products/<int:id>", methods=["GET"])
def get_by_id(id):
    return get_by_id_control(id)

@products_bp.route("/products", methods=["POST"])
def add_product():
    return add_product_control()

@products_bp.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    return update_product(id)

@products_bp.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    return delete_product(id)