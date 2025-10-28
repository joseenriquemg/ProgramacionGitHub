from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class Supermercado(BaseModel):
    id: int | None = None
    Fecha: date
    Superficie: float
    Direccion: str
    IdDirector: int

lista_supermercados = [
    Supermercado(id=1, Fecha=date(2023, 5, 10), Superficie=1200.5, Direccion="Calle Mayor 45, Madrid", IdDirector=1),
    Supermercado(id=2, Fecha=date(2022, 11, 2), Superficie=980.0, Direccion="Av. Andalucía 22, Sevilla", IdDirector=2),
    Supermercado(id=3, Fecha=date(2024, 3, 18), Superficie=1500.2, Direccion="Ronda Norte 15, Valencia", IdDirector=3),
    Supermercado(id=4, Fecha=date(2021, 7, 25), Superficie=800.0, Direccion="Gran Vía 101, Barcelona", IdDirector=4),
    Supermercado(id=5, Fecha=date(2023, 1, 5), Superficie=1100.0, Direccion="Calle Real 8, Málaga", IdDirector=5)
]

# FUNCIÓN PARA GENERAR NUEVO ID

def next_id():
    if not lista_supermercados:
        return 1
    return max(s.id for s in lista_supermercados) + 1

@app.get("/supermercados")
def obtener_supermercados():
    return lista_supermercados


@app.get("/supermercados/{id}")
def obtener_supermercado(id: int):
    for supermercado_guardado in lista_supermercados:
        if supermercado_guardado.id == id:
            return supermercado_guardado
    raise HTTPException(status_code=404, detail="Supermercado not found")

@app.post("/supermercados", status_code=201, response_model=Supermercado)
def supermercado(supermercado: Supermercado):
    supermercado.id = next_id()
    lista_supermercados.append(supermercado)
    return supermercado


@app.put("/supermercados/{id}")
def supermercado(id: int, supermercado: Supermercado):
    for index, supermercado_guardado in enumerate(lista_supermercados):
        if supermercado_guardado.id == id:
            supermercado.id = id
            lista_supermercados[index] = supermercado
            return supermercado
    raise HTTPException(status_code=404, detail="Supermercado not found")


@app.delete("/supermercados/{id}")
def supermercado(id: int):
    for supermercado_guardado in lista_supermercados:
        if supermercado_guardado.id == id:
            lista_supermercados.remove(supermercado_guardado)
            return {}
    raise HTTPException(status_code=404, detail="Supermercado not found")

