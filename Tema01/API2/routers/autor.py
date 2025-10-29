from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Autor(BaseModel):
    Id: int
    DNI: str
    Nombre: str
    Apellidos: str


lista_autores = [
    {"Id": 1, "DNI": "87654321F", "Nombre": "Fernando", "Apellidos": "Ruiz Morales"},
    {"Id": 2, "DNI": "98765432G", "Nombre": "Isabel", "Apellidos": "López Herrera"},
    {"Id": 3, "DNI": "76543210H", "Nombre": "Miguel", "Apellidos": "García Fernández"},
    {"Id": 4, "DNI": "65432109I", "Nombre": "Sofía", "Apellidos": "Martínez Domínguez"},
    {"Id": 5, "DNI": "54321098J", "Nombre": "David", "Apellidos": "Castillo Pérez"}
]

@router.get("/")
def obtener_autores():
    return lista_autores

@router.get("/{autor_id}")
def obtener_autor(autor_id: int):
    for a in lista_autores:
        if a.Id == autor_id:
            return a
    raise HTTPException(status_code=404, detail="Director no encontrado")   


