from backend.repositories.auth_repositories import login_repo
from werkzeug.security import check_password_hash

def login_services(username, password):
    user = login_repo(username)

    if user is None:
        return None

    password_hash = user["password"]

    if not check_password_hash(password_hash, password):
        return None

    return user