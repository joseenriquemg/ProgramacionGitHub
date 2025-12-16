from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.schemas.alumno import alumno_schema, alumnos_schema
from db.schemas.colegio import colegio_schema, colegios_schema
from db.models.colegio import Colegio

router = APIRouter(prefix="/colegios", tags=["colegios"])

class Colegio(BaseModel):
    Id: str
    Nombre: str
    Distrito: str
    Tipo: str
    Direccion: str


lista_colegios = [
    {"Id": "1", "Nombre": "Alonso Barba", "Distrito": "Sevilla", "Tipo": "publico", "Direccion": "Calle Sierpes"},
    {"Id": "2", "Nombre": "Nervion", "Distrito": "Sevilla", "Tipo": "concertado", "Direccion": "Calle Bujara"},
    {"Id": "3", "Nombre": "Martinez", "Distrito": "Sevilla", "Tipo": "privado", "Direccion": "Calle Melon"},
]

# Función para generar el próximo ID. Necesaria porque la lista no lo hace automáticamente.
def next_id():
    if not lista_colegios:
        return 1
    # Encuentra el ID más alto y suma 1. (NOTA: Esto fallará si 'lista_colegios' sigue siendo una lista de diccionarios 
    # y la lógica intenta acceder a 'c.id' en lugar de 'c["Id"]').
    return max(c.id for c in lista_colegios) + 1

# GET: Obtener todos los colegios (Ruta raíz del router)
@router.get("/")
def obtener_directorres():
    # Retorna la lista de diccionarios. FastAPI lo convierte a JSON automáticamente.
    return lista_colegios


# GET: Obtener un alumno por ID (Parámetro de Ruta)
@router.get("/{colegio_id}", response_model=Colegio)
def obtener_colegio(colegio_id: int): # 'colegio_id' se extrae de la URL 
    # Itera sobre la lista simulada
    for c in lista_colegios:
        # Compara el Id del dato guardado con el ID solicitado
        if c["Id"] == colegio_id: 
            return c # Retorna el diccionario encontrado
    
    # Si no se encuentra, lanza una excepción HTTP con código 404 (No encontrado)
    raise HTTPException(status_code=404, detail="Colegio no encontrado")

# POST: Crear un nuevo colegio
@router.post("/", status_code=201, response_model=Colegio)
def colegio(colegio: Colegio): # El cuerpo de la petición se valida como un objeto colegio
    
    # Asigna el ID generado por la función auxiliar
    colegio.Id = next_id()
    
    # Añade el nuevo objeto colegio a la lista (persistencia simulada)
    lista_colegios.append(colegio)
    
    # Retorna el objeto creado con el nuevo ID (código 201: Creado)
    return colegio


# PUT: Actualizar un colegio (Reemplazo completo)
@router.put("/{id}", response_model=Colegio)
def colegio(id: int, colegio: Colegio): # 'id' de la URL, 'colegio' del cuerpo de la petición
    
    # Itera sobre la lista usando enumerate para obtener el índice y el valor
    for index, colegio_guardado in enumerate(lista_colegios):
        # Busca el alumno por ID
        if colegio_guardado.Id == id: 
            
            # Asigna el ID de la URL al objeto entrante para asegurar consistencia
            colegio.Id = id
            
            # Reemplaza el elemento antiguo en la lista con el nuevo objeto
            lista_colegios[index] = colegio
            
            return colegio # Retorna el colegio actualizado
            
    # Si el ID no se encuentra
    raise HTTPException(status_code=404, detail="Colegio no encontrado")


# DELETE: Eliminar un alumno
@router.delete("/{id}")
def colegio(id: int):
    
    # Itera sobre la lista para encontrar el colegio a eliminar
    for colegio_guardado in lista_colegios:
        if colegio_guardado.Id == id:
            # Elimina el objeto de la lista (simulación de borrado)
            lista_colegios.remove(colegio_guardado)
            
            # Retorna un cuerpo vacío ({}) con código 204 (No Content), indicando éxito
            return {} 
            
    # Si el ID no se encuentra
    raise HTTPException(status_code=404, detail="Colegio no encontrado")


