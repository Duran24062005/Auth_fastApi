from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def app_cors(app: FastAPI):
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
