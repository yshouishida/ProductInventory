from backend.services.auth_services import login_services
from backend.utils.api_response import success, error
from flask import request


def login_control():
    user_input = request.get_json()

    if user_input is None:
        return error("Username and Password are required.", 400)

    username = user_input.get("username")
    password = user_input.get("password")

    get_user = login_services(username, password)

    if get_user is None:
        return error("Invalid username or password.", 401)

    return success("Login successfully.", 200, get_user)



