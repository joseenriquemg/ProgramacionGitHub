from fastapi import APIRouter, HTTPException, status # Importamos APIRouter, HTTPException para errores, y status para códigos HTTP legibles
from pydantic import BaseModel # Importamos BaseModel para definir la estructura de la entidad (Director)
from typing import List, Optional # Importamos List y Optional para tipos de datos más claros

# --- 1. CONFIGURACIÓN DEL ROUTER Y MODELO ---

# Inicializamos el APIRouter. Esto modulariza la API y permite agrupar rutas.
router = APIRouter(prefix="/directores", tags=["directores"])

# Definición de la Entidad Director usando Pydantic (Modelo de Datos)
class Director(BaseModel):
    # Id: Entero. Se usa 'int | None = None' para Python 3.10+ o 'Optional[int] = None' para versiones anteriores. 
    # Esto indica que el ID es opcional al crear un director (POST).
    Id: int | None = None
    DNI: str 
    Nombe: str # NOTA: Aquí hay un error tipográfico, debería ser 'Nombre'
    Apellido: str
    email: str

# --- 2. SIMULACIÓN DE LA BASE DE DATOS (LISTA EN MEMORIA) ---

# Lista de diccionarios que simula la base de datos (DB). Los datos iniciales están en formato diccionario.
lista_directores = [
    {"Id": 1, "DNI": "12345678A", "Nombre": "Laura", "Apellidos": "Gómez Ruiz", "email": "laura.gomez@empresa.com"},
    {"Id": 2, "DNI": "23456789B", "Nombre": "Carlos", "Apellidos": "Martínez López", "email": "carlos.martinez@empresa.com"},
    {"Id": 3, "DNI": "34567890C", "Nombre": "María", "Apellidos": "Fernández Pérez", "email": "maria.fernandez@empresa.com"},
    {"Id": 4, "DNI": "45678901D", "Nombre": "Javier", "Apellidos": "Sánchez Torres", "email": "javier.sanchez@empresa.com"},
    {"Id": 5, "DNI": "56789012E", "Nombre": "Ana", "Apellidos": "Castillo Ramos", "email": "ana.castillo@empresa.com"}
]

# --- 3. FUNCIÓN AUXILIAR (Lógica para POST) ---

# Función para generar el próximo ID. Necesaria porque la lista no lo hace automáticamente.
def next_id():
    if not lista_directores:
        return 1
    # Encuentra el ID más alto y suma 1. (NOTA: Esto fallará si 'lista_directores' sigue siendo una lista de diccionarios 
    # y la lógica intenta acceder a 'd.id' en lugar de 'd["Id"]').
    return max(d.id for d in lista_directores) + 1 # Error potencial: Intenta acceder al atributo 'id' en un diccionario

# --- 4. ENDPOINTS (OPERACIONES CRUD) ---

# GET: Obtener todos los directores (Ruta raíz del router)
@router.get("/")
def obtener_directorres():
    # Retorna la lista de diccionarios. FastAPI lo convierte a JSON automáticamente.
    return lista_directores


# GET: Obtener un director por ID (Parámetro de Ruta)
@router.get("/{director_id}", response_model=Director)
def obtener_director(director_id: int): # 'director_id' se extrae de la URL (ej: /directores/1)
    # Itera sobre la lista simulada
    for d in lista_directores:
        # Compara el Id del dato guardado con el ID solicitado
        if d["Id"] == director_id: 
            return d # Retorna el diccionario encontrado
    
    # Si no se encuentra, lanza una excepción HTTP con código 404 (No encontrado)
    raise HTTPException(status_code=404, detail="Director no encontrado")

# POST: Crear un nuevo director
@router.post("/", status_code=201, response_model=Director)
def director(director: Director): # El cuerpo de la petición se valida como un objeto Director
    
    # Asigna el ID generado por la función auxiliar
    director.Id = next_id()
    
    # Añade el nuevo objeto Director a la lista (persistencia simulada)
    lista_directores.append(director)
    
    # Retorna el objeto creado con el nuevo ID (código 201: Creado)
    return director


# PUT: Actualizar un director (Reemplazo completo)
@router.put("/{id}", response_model=Director)
def director(id: int, director: Director): # 'id' de la URL, 'director' del cuerpo de la petición
    
    # Itera sobre la lista usando enumerate para obtener el índice y el valor
    for index, director_guardado in enumerate(lista_directores):
        # Busca el director por ID
        if director_guardado.Id == id: 
            
            # Asigna el ID de la URL al objeto entrante para asegurar consistencia
            director.Id = id
            
            # Reemplaza el elemento antiguo en la lista con el nuevo objeto
            lista_directores[index] = director
            
            return director # Retorna el director actualizado
            
    # Si el ID no se encuentra
    raise HTTPException(status_code=404, detail="Director no encontrado")


# DELETE: Eliminar un director
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def director(id: int):
    
    # Itera sobre la lista para encontrar el director a eliminar
    for director_guardado in lista_directores:
        if director_guardado.Id == id:
            # Elimina el objeto de la lista (simulación de borrado)
            lista_directores.remove(director_guardado)
            
            # Retorna un cuerpo vacío ({}) con código 204 (No Content), indicando éxito
            return {} 
            
    # Si el ID no se encuentra
    raise HTTPException(status_code=404, detail="Director no encontrado")