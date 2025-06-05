from fastapi import FastAPI, Form, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.exceptions import HTTPException

app = FastAPI(
    title="Authentication in FastAPI",
    version="0.0.1"
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

users = {
    "alexi": {"username": "alexi", "email": "alexisoft01@gmail.com", "password": "hxk65d"},
    "user2": {"username": "user2", "email": "user2soft01@gmail.com", "password": "hxk65d"}
}

def enconde_token(payloas: dict)->str:
    return "hthskjsuejene"

def decode_token(token: Annotated[str, Depends(oauth2_schema)])-> dict:
    return users.get('alexi')

@app.get('/', status_code=200)
async def root():
    return "Hello world¡¡"

@app.post('/token2', status_code=200)
async def login2(username = Form(), password = Form()):
    return f"Usuario {username} con password {password}"

@app.post('/token', status_code=200)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username")
    token = enconde_token({"username": user['username'], "email": user['email']})
    return { "access_token": token }


@app.get('/users/profile', status_code=200)
async def profile(my_user: Annotated[dict, Depends(decode_token)]):
    return my_user