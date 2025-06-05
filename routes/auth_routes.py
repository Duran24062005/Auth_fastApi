from fastapi import APIRouter, Form, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.exceptions import HTTPException
from middlewares.jwt_manager import enconde_token, decode_token
from db.users import users


auth_routes = APIRouter()

@auth_routes.get('/', status_code=200)
async def root():
    return "Hello world¡¡"

@auth_routes.post('/token2', status_code=200)
async def login2(username = Form(), password = Form()):
    return f"Usuario {username} con password {password}"

@auth_routes.post('/token', status_code=200)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(form_data.username)
    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = enconde_token({"username": user['username'], "email": user['email']})
    return { "access_token": token }


@auth_routes.get('/users/profile', response_model=dict, status_code=200)
async def profile(my_user: Annotated[dict, Depends(decode_token)])->dict:
    return my_user