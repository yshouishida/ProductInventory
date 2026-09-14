from backend.repositories.products_repository import (
    get_products_repo,
    get_by_id_repo,
    add_product_repo,
    update_product_repo,
    delete_product_repo
)

def get_products_service():
    return get_products_repo()

def get_by_id_service(id):
    return get_by_id_repo(id)

def add_product_service(code, name, description, qty, price):
    return add_product_repo(code, name, description, qty, price)

def update_product_service(code, name, description, qty, price, id):
    result = update_product_repo(code, name, description, qty, price, id)

    if not result:
        return None

    return result

def delete_product_service(id):
    result = delete_product_repo(id)

    if not result:
        return None

    return result


