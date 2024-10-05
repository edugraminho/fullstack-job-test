import redis
from fastapi import HTTPException
import os

r = redis.Redis(host="redis", port=6379, db=0)

TOKEN_EXPIRATION_SECONDS = int(os.getenv("TOKEN_EXPIRATION_SECONDS"))


def store_access_token(token: str):
    r.set("access_token", token, ex=TOKEN_EXPIRATION_SECONDS)


def get_access_token():
    token = r.get("access_token")
    if token is None:
        raise HTTPException(
            status_code=401, detail="Access token not found, please log in"
        )
    return token.decode("utf-8")
