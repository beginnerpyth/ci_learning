from datetime import UTC, datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from database import settings

token_url = OAuth2PasswordBearer(tokenUrl="/login")
alg = "HS256"
TOKEN_EXPIRE_MINUTES = 30
secret_key = settings.secret_key


def token_creator(real_data: dict):
    copy_data = real_data.copy()  # only inside dict there is copy()

    exp_time = datetime.now(UTC) + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    copy_data.update({"exp": exp_time})  # passing the expire data inform of dictionary

    jwt_created = jwt.encode(copy_data, secret_key, algorithm=alg)
    return jwt_created


def token_decoder(real_token: str = Depends(token_url)):
    try:
        copy_token = jwt.decode(real_token, secret_key, algorithms=[alg])
    except JWTError:
        raise HTTPException(status_code=401, detail="invalid or expired token")
    return {
        "email": copy_token.get("email"),
        "name": copy_token.get("name"),
        "role": copy_token.get("role"),
    }


def token_verifier(real_role: str):  # we placed nondefault parameter at first its rule
    def token_compare(token_converter: dict = Depends(token_decoder)):
        if token_converter["role"] != real_role:
            raise HTTPException(
                status_code=403,
                detail=(f"you are forbidden as {token_converter['name']}"),
            )
        return real_role

    return token_compare
