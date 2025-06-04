from fastapi import FastAPI

app = FastAPI(
    title="Authentication in FastAPI",
    version="0.0.1"
)


@app.get('/')
async def root():
    return "Hello world¡¡"