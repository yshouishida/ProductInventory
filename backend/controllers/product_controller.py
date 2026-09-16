from flask import request
from decimal import Decimal, InvalidOperation

from backend.utils.api_response import success, error
from backend.services.product_services import (
    get_products_service,
    get_by_id_service,
    add_product_service,
    update_product_service,
    delete_product_service
)

def get_products_control():
    products = get_products_service()
    return success("Products retrieved successfully.", 200, products)

def get_by_id_control(id):
    product = get_by_id_service(id)

    if product is None:
        return error("Product is not found.", 404)

    return success("Product retrieved successfully.", 200, product)


def _product_data():
    product = request.get_json(silent=True)
    if not isinstance(product, dict):
        return None
    if not isinstance(product.get("code"), str) or not product["code"].strip() or len(product["code"]) > 20:
        return None
    if not isinstance(product.get("name"), str) or not product["name"].strip() or len(product["name"]) > 100:
        return None
    if product.get("description") is not None and not isinstance(product["description"], str):
        return None
    qty = product.get("qty")
    price = product.get("price")
    if isinstance(qty, bool) or not isinstance(qty, int) or qty < 0:
        return None
    try:
        amount = Decimal(str(price))
    except (InvalidOperation, TypeError, ValueError):
        return None
    if isinstance(price, bool) or not amount.is_finite() or amount < 0 or amount > Decimal("99999999.99") or amount.as_tuple().exponent < -2:
        return None
    return product

def add_product_control():
    product = _product_data()
    if product is None:
        return error("Invalid product. Provide code, name, nonnegative integer qty, and nonnegative price with at most two decimal places.", 400)

    add_product_service(
        product.get("code"),
        product.get("name"),
        product.get("description"),
        product.get("qty"),
        product.get("price")
    )

    return success("Added successfully.", 201)
    
def update_product_control(id): 
    product = _product_data()
    if product is None:
        return error("Invalid product. Provide code, name, nonnegative integer qty, and nonnegative price with at most two decimal places.", 400)

    result = update_product_service(
        product.get("code"),
        product.get("name"),
        product.get("description"),
        product.get("qty"),
        product.get("price"),
        id
    )

    if not result:
        return error("Product is not found.", 404)

    return success("Updated successfully.", 200)

def delete_product_control(id): 
    result = delete_product_service(id)

    if not result:
        return error("Product is not found.", 404)

    return success("Deleted successfully.", 200)
