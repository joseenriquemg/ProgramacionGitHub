from fastapi import  FastAPI
from routers import autor, libro
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(autor.router)
app.include_router(libro.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def inicio():
    return {"Hello": "Wordl"}