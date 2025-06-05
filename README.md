# Authentication in FastAPI - Práctica de Aprendizaje

Este proyecto es una implementación mejorada de autenticación con FastAPI, creado con fines educativos para aprender los conceptos fundamentales de autenticación en APIs REST con mejores prácticas de seguridad.

## 📋 Descripción

Esta aplicación demuestra conceptos más avanzados de autenticación en FastAPI, incluyendo:
- Autenticación basada en tokens JWT (JSON Web Tokens)
- Manejo seguro de variables de entorno
- Configuración CORS para aplicaciones frontend
- Protección de rutas con dependencias
- Validación mejorada de credenciales

## 🚀 Características

- **Tokens JWT reales**: Implementación con la librería `python-jose` para tokens seguros
- **Variables de entorno**: Manejo seguro de claves secretas con `python-dotenv`
- **Middleware CORS**: Configuración para permitir peticiones desde aplicaciones frontend
- **Validación mejorada**: Verificación tanto de usuario como contraseña
- **Decodificación de tokens**: Extracción segura de información del payload JWT

## 📁 Estructura del Proyecto

```
proyecto/
├── main.py          # Archivo principal con la aplicación FastAPI
├── requirements.txt # Dependencias del proyecto
├── .env            # Variables de entorno (NO incluir en Git)
├── .gitignore      # Archivos y carpetas a ignorar por Git
└── README.md       # Este archivo
```

## 🛠️ Instalación y Ejecución

### Prerrequisitos
- Python 3.7+
- pip

### Pasos de instalación

1. Clona el repositorio o descarga los archivos
2. Crea un archivo `.env` en la raíz del proyecto:
   ```
   MY_SECRET_KEY=tu_clave_secreta_muy_segura_aqui
   ALGORITHM=HS256
   ```
3. Instala las dependencias:
   ```bash
   pip install fastapi uvicorn python-multipart python-jose[cryptography] python-dotenv
   ```
4. Ejecuta la aplicación:
   ```bash
   uvicorn main:app --reload
   ```
5. Abre tu navegador en `http://127.0.0.1:8000`

## 📚 Endpoints Disponibles

### 🔓 Públicos

- **GET /**: Endpoint de bienvenida
  - Respuesta: `"Hello world¡¡"`

### 🔐 Autenticación

- **POST /token**: Login principal con OAuth2 y JWT
  - Requiere: `username` y `password` en formato OAuth2PasswordRequestForm
  - Retorna: Token JWT válido con información del usuario
  - Validación: Verifica tanto usuario como contraseña
  
- **POST /token2**: Login alternativo con formulario simple
  - Requiere: `username` y `password` como campos de formulario
  - Retorna: Mensaje de confirmación

### 🔒 Protegidos

- **GET /users/profile**: Perfil del usuario autenticado
  - Requiere: Token JWT válido en el header Authorization
  - Retorna: Información completa del usuario desde el token decodificado

## 👥 Usuarios de Prueba

El sistema incluye dos usuarios predefinidos para testing:

| Username | Email | Password |
|----------|-------|----------|
| alexi | alexisoft01@gmail.com | hxk65d |
| user2 | user2soft01@gmail.com | hxk65d |

## 🔧 Cómo Usar la API

### 1. Obtener un token

```bash
curl -X POST "http://127.0.0.1:8000/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=alexi&password=hxk65d"
```

### 2. Usar el token JWT para acceder al perfil

```bash
curl -X GET "http://127.0.0.1:8000/users/profile" \
     -H "Authorization: Bearer tu_token_jwt_aqui"
```

### 3. Ejemplo con frontend (JavaScript)

```javascript
// Login
const response = await fetch('http://127.0.0.1:8000/token', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: 'username=alexi&password=hxk65d'
});
const data = await response.json();
const token = data.access_token;

// Acceder al perfil
const profileResponse = await fetch('http://127.0.0.1:8000/users/profile', {
    headers: {
        'Authorization': `Bearer ${token}`
    }
});
const profile = await profileResponse.json();
```

## 📖 Conceptos Aprendidos

Este proyecto cubre los siguientes conceptos avanzados de autenticación:

1. **JWT (JSON Web Tokens)**: Implementación real con `python-jose`
2. **Variables de entorno**: Manejo seguro de claves con `python-dotenv`
3. **CORS Middleware**: Configuración para aplicaciones web modernas
4. **OAuth2PasswordBearer**: Esquema de autenticación OAuth2
5. **OAuth2PasswordRequestForm**: Formulario estándar para credenciales
6. **Dependencias en FastAPI**: Uso avanzado de `Depends()` para inyección
7. **Validación de credenciales**: Verificación completa de usuario y contraseña
8. **Decodificación segura**: Extracción de payload desde tokens JWT

## ⚠️ Notas Importantes

**Este sigue siendo un proyecto educativo** con algunas implementaciones que necesitan mejoras para producción:

- Las contraseñas están en texto plano (usar hashing en producción)
- Los usuarios están hardcodeados en memoria (usar base de datos)
- No hay validación de expiración de tokens JWT
- La clave secreta debe ser más compleja en producción
- Falta manejo de refresh tokens

## ✅ Mejoras Implementadas

Comparado con la versión anterior, ahora incluye:
- ✅ **Tokens JWT reales** en lugar de tokens estáticos
- ✅ **Variables de entorno** para claves secretas
- ✅ **Middleware CORS** para aplicaciones frontend
- ✅ **Validación completa** de usuario y contraseña
- ✅ **Decodificación segura** de tokens JWT

## 🎯 Próximos Pasos para Mejorar

Para un proyecto real, considera implementar:

1. **Hashing de contraseñas** con bcrypt o argon2
2. **Expiración de tokens JWT** con manejo de tiempo
3. **Base de datos** real para usuarios (PostgreSQL, MongoDB)
4. **Refresh tokens** para renovación automática
5. **Middleware de rate limiting** para prevenir ataques
6. **Validación de entrada** más robusta con Pydantic
7. **Logging y monitoreo** de intentos de autenticación
8. **Tests unitarios** para endpoints de autenticación

## 🔒 Configuración de Seguridad

### Variables de Entorno Requeridas

Crea un archivo `.env` con las siguientes variables:

```env
# Clave secreta para firmar los tokens JWT
MY_SECRET_KEY=tu_clave_secreta_muy_larga_y_compleja_aqui_con_al_menos_32_caracteres

# Algoritmo para JWT
ALGORITHM=HS256
```

### CORS Configuration

La aplicación está configurada para permitir peticiones desde:
- `http://localhost:3000` (React development)
- `http://localhost:5173` (Vite development)  
- `https://tudominio.com` (Producción - personalizar según necesites)

## 📦 Dependencias

FastAPI genera automáticamente documentación interactiva:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 🤝 Contribuciones

Este es un proyecto de aprendizaje. Si encuentras mejoras o errores, siéntete libre de sugerir cambios.

---

**Autor**: Estudiante de FastAPI Authentication  
**Propósito**: Práctica educativa de autenticación web