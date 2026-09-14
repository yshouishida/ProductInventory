import jwt
import uuid
from datetime import datetime, timedelta, timezone
from backend.utils.api_response import success, error
from backend.config.settings import JWT_SECRET_KEY, JWT_TOKEN_EXPIRED
from backend.utils.JWT_TOKEN_BLOCKLIST import JWT_TOKEN_BLOCKLIST
from flask import request, g
from functools import wraps




def create_access_token(identity, role):
    jti = str(uuid.uuid4())
    payload = {
        "sub": str(identity),
        "jti": jti,
        "exp": datetime.now(timezone.utc) + timedelta(seconds=JWT_TOKEN_EXPIRED),
        "role": role
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=["HS256"])
    return token

def token_required(f):
    @wraps(f)

    def decorated(*args, **kwargs):
        header = request.headers.get("Authorization")
        if header.startswith("Bearer "):
            return error("Authorization is required.", 401)
        token = header.split(" ")[1]

        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
            jti = payload.get("jti")
            if jti in JWT_TOKEN_BLOCKLIST:
                return error("Token has been revoked.", 401)
            g.jti = jti
            g.payload = payload
            g.user_id = int(payload.get("sub"))
            g.user_role = payload.get("role")
            
        except jwt.ExpiredSignatureError:
            return error("Token has been expired. Please login again.", 401)

        return f(*args, **kwargs)
    return decorated
            