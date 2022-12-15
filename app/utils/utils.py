from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # should be kept secret
JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY")  # should be kept secret

# bcrypt text
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# function to convert plain password into hash password
def password_hash(password: str) -> str:
    return password_context.hash(password)


# compair logging password with hash password
def verify_password(password: str, hash_password: str) -> str:
    return password_context.verify(password, hash_password)


# create tokens
def create_access_token(subject: Union[str, Any], expire_delta: int = None) -> str:

    if expire_delta is not None:
        expire_delta = datetime.utcnow() + expire_delta
    else:
        expire_delta = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expire_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)

    return encoded_jwt


# refresh tokens
def refresh_access_token(subject: Union[str, Any], expire_delta: int = None) -> str:

    if expire_delta is not None:
        expire_delta = datetime.utcnow() + expire_delta
    else:
        expire_delta = datetime.utcnow() + timedelta(
            minutes=REFRESH_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expire_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)

    return encoded_jwt
