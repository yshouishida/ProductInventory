from backend.services.auth_services import login_services
from backend.utils.api_response import success, error
from flask import request


def login_control():
    user_input = request.get_json(silent=True)

    if not isinstance(user_input, dict):
        return error("Username and password are required.", 400)

    username = user_input.get("username")
    password = user_input.get("password")
    if not isinstance(username, str) or not username.strip() or len(username.strip()) > 100 or not isinstance(password, str) or not password:
        return error("Username and password are required.", 400)

    login_data = login_services(username.strip(), password)

    if login_data is None:
        return error("Invalid username or password.", 401)

    return success("Login successful.", 200, login_data)



