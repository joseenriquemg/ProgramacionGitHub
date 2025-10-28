from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Director(BaseModel):
    Id: int
    DNI: str 
    Nombe: str
    Apellido: str
    email: str

lista_directores = [
    {"Id": 1, "DNI": "12345678A", "Nombre": "Laura", "Apellidos": "Gómez Ruiz", "email": "laura.gomez@empresa.com"},
    {"Id": 2, "DNI": "23456789B", "Nombre": "Carlos", "Apellidos": "Martínez López", "email": "carlos.martinez@empresa.com"},
    {"Id": 3, "DNI": "34567890C", "Nombre": "María", "Apellidos": "Fernández Pérez", "email": "maria.fernandez@empresa.com"},
    {"Id": 4, "DNI": "45678901D", "Nombre": "Javier", "Apellidos": "Sánchez Torres", "email": "javier.sanchez@empresa.com"},
    {"Id": 5, "DNI": "56789012E", "Nombre": "Ana", "Apellidos": "Castillo Ramos", "email": "ana.castillo@empresa.com"}
]

def next_id():
    if not lista_directores:
        return 1
    return max(d.id for d in lista_directores) + 1



@app.get("/directores")
def obtener_directorres():
    return lista_directores


@app.get("/directores/{director_id}")
def obtener_director(director_id: int):
    for d in lista_directores:
        if d.Id == director_id:
            return d
    raise HTTPException(status_code=404, detail="Director no encontrado")   

@app.post("/directores", status_code=201, response_model=Director)
def director(director: Director):
    director.id = next_id()
    lista_directores.append(director)
    return director


@app.put("/directores/{id}")
def director(id: int, director: Director):
    for index, director_guardado in enumerate(lista_directores):
        if director_guardado.id == id:
            director.id = id
            lista_directores[index] = director
            return director
    raise HTTPException(status_code=404, detail="Director no encontrado")


@app.delete("/directores/{id}")
def director(id: int):
    for director_guardado in lista_directores:
        if director_guardado.id == id:
            lista_directores.remove(director_guardado)
            return {}
    raise HTTPException(status_code=404, detail="Director no encontrado")
