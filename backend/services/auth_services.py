from backend.repositories.auth_repositories import login_repo
from backend.utils.jwt_utils import create_access_token
from werkzeug.security import check_password_hash

def login_services(email, password):
    user = login_repo(email)

    if user is None:
        return None

    if not check_password_hash(user["password"], password):
        return None

    return {
        "access_token": create_access_token(user["id"], user["role"]),
        "user": {
            "id": user["id"],
            "email": user["email"],
            "role": user["role"],
        },
    }
