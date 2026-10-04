from backend.services.auth_services import login_services
from backend.utils.api_response import success, error
from flask import request


def login_control():
    user_input = request.get_json(silent=True)

    if not isinstance(user_input, dict):
        return error("Email and password are required.", 400)

    email = user_input.get("email")
    password = user_input.get("password")
    if not isinstance(email, str) or not email.strip() or len(email.strip()) > 100 or not isinstance(password, str) or not password:
        return error("email and password are required.", 400)

    login_data = login_services(email.strip(), password)

    if login_data is None:
        return error("Invalid email or password.", 401)

    return success("Login successful.", 200, login_data)



