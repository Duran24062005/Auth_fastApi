from fastapi import FastAPI, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.exceptions import HTTPException
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

my_secret_key = os.getenv("MY_SECRET_KEY")
algorithm = os.getenv("ALGORITHM")

app = FastAPI(
    title="Authentication in FastAPI",
    version="0.0.1"
)

# Lista de orígenes permitidos
origins = [
    "http://localhost:3000",  # React local
    "http://localhost:5173",  # Vite local
    "https://tudominio.com"   # Producción (si aplica)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # Orígenes permitidos
    allow_credentials=True,             # Cookies/autenticación
    allow_methods=["*"],                # Métodos HTTP permitidos
    allow_headers=["*"],                # Encabezados permitidos
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

users = {
    "alexi": {"username": "alexi", "email": "alexisoft01@gmail.com", "password": "hxk65d"},
    "user2": {"username": "user2", "email": "user2soft01@gmail.com", "password": "hxk65d"}
}

def enconde_token(payload: dict)->str:
    token = jwt.encode(payload, key=my_secret_key, algorithm=algorithm)
    return token

def decode_token(token: Annotated[str, Depends(oauth2_schema)])-> dict:
    data = jwt.decode(token=token, key=my_secret_key, algorithms=[algorithm])
    user = users.get(data['username'])
    return user

@app.get('/', status_code=200)
async def root():
    return "Hello world¡¡"

@app.post('/token2', status_code=200)
async def login2(username = Form(), password = Form()):
    return f"Usuario {username} con password {password}"

@app.post('/token', status_code=200)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(form_data.username)
    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = enconde_token({"username": user['username'], "email": user['email']})
    return { "access_token": token }


@app.get('/users/profile', response_model=dict, status_code=200)
async def profile(my_user: Annotated[dict, Depends(decode_token)])->dict:
    return my_user