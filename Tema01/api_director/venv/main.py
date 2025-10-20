from fastapi import FastAPI, HTTPException
from typing import List

# Crear la aplicación
app = FastAPI(
    title="API de Directores",
    description="API REST con FastAPI para gestionar información de directores",
    version="1.0.0"
)

# Datos de ejemplo (como si fueran de una base de datos)
directores = [
    {"Id": 1, "DNI": "12345678A", "Nombre": "Pedro", "Apellidos": "López García", "Email": "pedro@example.com"},
    {"Id": 2, "DNI": "87654321B", "Nombre": "María", "Apellidos": "Pérez Torres", "Email": "maria@example.com"},
    {"Id": 3, "DNI": "11223344C", "Nombre": "Juan", "Apellidos": "Martín Ruiz", "Email": "juan@example.com"},
]


# Ruta principal (opcional)
@app.get("/")
def raiz():
    return {"mensaje": "Bienvenido a la API de Directores"}


# ✅ GET 1: Obtener todos los directores
@app.get("/directores", tags=["Directores"])
def obtener_directores() -> List[dict]:
    return directores


# ✅ GET 2: Obtener un director por su ID
@app.get("/directores/{id}", tags=["Directores"])
def obtener_director(id: int):
    for d in directores:
        if d["Id"] == id:
            return d
    raise HTTPException(status_code=404, detail="Director no encontrado")