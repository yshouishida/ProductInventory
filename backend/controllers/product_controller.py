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

    if products is None:
        return error("Products are not found.", 404)

    return success("Get successfully", 200, products)

def get_by_id_control(id):
    product = get_by_id_service(id)

    if product is None:
        return error("Product is not found.", 404)

    return success("Get successfully.", 404, product)

def add_product_control():
    result = add_product_service()

    if result is None:
        return error("Unable to add product.", 400)

    return success("Added successfully.", 201)
    
def update_product_control(id): 
    result = update_product_service(id)

    if result is None:
        return error("Unable to update product.", 400)

    return success("Updated successfully.", 200)

def delete_product_control(id): 
    result = delete_product_service(id)

    if result is None:
        return error("Unable to delete product.", 400)

    return success("Deleted sucessfully.", 200)