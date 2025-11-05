from fastapi import FastAPI
from routers import director, supermercado, auth_users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(director.router)
app.include_router(supermercado.router)
app.include_router(auth_users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def inicio():
    return {"Hello": "Wordl"}