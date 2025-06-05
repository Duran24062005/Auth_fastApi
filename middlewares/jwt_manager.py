from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.exceptions import HTTPException
from jose import jwt
from dotenv import load_dotenv
import os
from db.users import users


load_dotenv()

my_secret_key = os.getenv("MY_SECRET_KEY")
algorithm = os.getenv("ALGORITHM")

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

def enconde_token(payload: dict)->str:
    token = jwt.encode(payload, key=my_secret_key, algorithm=algorithm)
    return token

def decode_token(token: Annotated[str, Depends(oauth2_schema)])-> dict:
    data = jwt.decode(token=token, key=my_secret_key, algorithms=[algorithm])
    user = users.get(data['username'])
    return user