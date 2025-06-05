# Authentication in FastAPI - Práctica de Aprendizaje

Este proyecto es una implementación básica de autenticación con FastAPI, creado con fines educativos para aprender los conceptos fundamentales de autenticación en APIs REST.

## 📋 Descripción

Esta aplicación demuestra los conceptos básicos de autenticación en FastAPI, incluyendo:
- Autenticación basada en tokens OAuth2
- Manejo de formularios de login
- Protección de rutas con dependencias
- Estructura básica de usuarios y tokens

## 🚀 Características

- **Autenticación OAuth2**: Implementación del flujo de autenticación estándar
- **Múltiples endpoints de login**: Dos formas diferentes de manejar el login
- **Protección de rutas**: Endpoint protegido que requiere autenticación
- **Gestión de usuarios**: Sistema básico de usuarios en memoria

## 📁 Estructura del Proyecto

```
proyecto/
├── main.py          # Archivo principal con la aplicación FastAPI
├── requirements.txt # Dependencias del proyecto
├── .gitignore      # Archivos y carpetas a ignorar por Git
└── README.md       # Este archivo
```

## 🛠️ Instalación y Ejecución

### Prerrequisitos
- Python 3.7+
- pip

### Pasos de instalación

1. Clona el repositorio o descarga los archivos
2. Instala las dependencias:
   ```bash
   pip install fastapi uvicorn python-multipart
   ```
3. Ejecuta la aplicación:
   ```bash
   uvicorn main:app --reload
   ```
4. Abre tu navegador en `http://127.0.0.1:8000`

## 📚 Endpoints Disponibles

### 🔓 Públicos

- **GET /**: Endpoint de bienvenida
  - Respuesta: `"Hello world¡¡"`

### 🔐 Autenticación

- **POST /token**: Login principal con OAuth2
  - Requiere: `username` y `password` en formato OAuth2PasswordRequestForm
  - Retorna: Token de acceso
  
- **POST /token2**: Login alternativo con formulario simple
  - Requiere: `username` y `password` como campos de formulario
  - Retorna: Mensaje de confirmación

### 🔒 Protegidos

- **GET /users/profile**: Perfil del usuario autenticado
  - Requiere: Token válido en el header Authorization
  - Retorna: Información del usuario

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

### 2. Usar el token para acceder al perfil

```bash
curl -X GET "http://127.0.0.1:8000/users/profile" \
     -H "Authorization: Bearer tu_token_aqui"
```

## 📖 Conceptos Aprendidos

Este proyecto cubre los siguientes conceptos de autenticación:

1. **OAuth2PasswordBearer**: Esquema de autenticación OAuth2
2. **OAuth2PasswordRequestForm**: Formulario estándar para credenciales
3. **Dependencias en FastAPI**: Uso de `Depends()` para inyección de dependencias
4. **Tokens de acceso**: Generación y validación básica de tokens
5. **Protección de rutas**: Cómo proteger endpoints específicos
6. **Manejo de errores**: HTTPException para errores de autenticación

## ⚠️ Notas Importantes

**Este es un proyecto educativo** con implementaciones simplificadas:

- Los tokens son estáticos (no seguros para producción)
- Las contraseñas están en texto plano (usar hashing en producción)
- Los usuarios están hardcodeados en memoria
- No hay validación real de tokens
- Falta manejo de expiración de tokens

## 🎯 Próximos Pasos para Mejorar

Para un proyecto real, considera implementar:

1. **Hashing de contraseñas** con bcrypt
2. **JWT tokens** reales con expiración
3. **Base de datos** para usuarios
4. **Middleware de seguridad** adicional
5. **Refresh tokens** para renovación
6. **Validación de entrada** más robusta

## 📄 Documentación Interactiva

FastAPI genera automáticamente documentación interactiva:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 🤝 Contribuciones

Este es un proyecto de aprendizaje. Si encuentras mejoras o errores, siéntete libre de sugerir cambios.

---

**Autor**: Estudiante de FastAPI Authentication  
**Propósito**: Práctica educativa de autenticación web