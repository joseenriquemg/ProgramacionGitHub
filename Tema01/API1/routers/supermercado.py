from fastapi import APIRouter, HTTPException, status # Importamos status para usar códigos HTTP legibles
from pydantic import BaseModel # Necesario para definir la estructura de la entidad
from datetime import date # Necesario para manejar el tipo de dato 'date'
from typing import List, Optional # Necesario para declarar listas de tipos y campos opcionales

# --- 1. CONFIGURACIÓN DEL ROUTER Y MODELO ---

# Inicializamos el APIRouter con un prefijo (/supermercados) y una etiqueta (tags)
router = APIRouter(prefix="/supermercados", tags=["supermercados"])

# Definición de la Entidad Supermercado usando Pydantic (Modelo de Datos)
class Supermercado(BaseModel):
    # ID: Opcional (se genera al hacer POST) y de tipo entero.
    id: Optional[int] = None 
    Fecha: date # Fecha de registro/apertura (Pydantic valida el formato de fecha)
    Superficie: float
    Direccion: str
    IdDirector: int # Clave foránea que relaciona con la entidad Director

# --- 2. SIMULACIÓN DE LA BASE DE DATOS (LISTA EN MEMORIA) ---

# Creamos una lista de objetos Supermercado para simular la base de datos
lista_supermercados = [
    Supermercado(id=1, Fecha=date(2023, 5, 10), Superficie=1200.5, Direccion="Calle Mayor 45, Madrid", IdDirector=1),
    Supermercado(id=2, Fecha=date(2022, 11, 2), Superficie=980.0, Direccion="Av. Andalucía 22, Sevilla", IdDirector=2),
    Supermercado(id=3, Fecha=date(2024, 3, 18), Superficie=1500.2, Direccion="Ronda Norte 15, Valencia", IdDirector=3),
    Supermercado(id=4, Fecha=date(2021, 7, 25), Superficie=800.0, Direccion="Gran Vía 101, Barcelona", IdDirector=4),
    Supermercado(id=5, Fecha=date(2023, 1, 5), Superficie=1100.0, Direccion="Calle Real 8, Málaga", IdDirector=5)
]

# --- 3. FUNCIÓN AUXILIAR ---

# Función para generar el próximo ID disponible para un nuevo recurso
def next_id():
    if not lista_supermercados:
        return 1
    # Busca el ID más alto en la lista y le suma 1 (Restricción de No Estado ignorada para este ejemplo)
    return max(s.id for s in lista_supermercados) + 1

# --- 4. ENDPOINTS (OPERACIONES CRUD) ---

# GET: Obtener todos los supermercados
@router.get("/", response_model=List[Supermercado])
def obtener_supermercados():
    # Devuelve la lista completa. FastAPI automáticamente serializa los objetos Pydantic a JSON.
    return lista_supermercados


# GET: Obtener un supermercado por ID (Parámetro de Ruta)
@router.get("/{id}", response_model=Supermercado)
def obtener_supermercado(id: int): # 'id' se recibe como parámetro de ruta
    # Itera sobre la lista para buscar el supermercado con el ID coincidente
    for supermercado_guardado in lista_supermercados:
        if supermercado_guardado.id == id:
            return supermercado_guardado # Retorna el objeto encontrado
    
    # Si el bucle termina sin encontrar el ID, lanza la excepción 404
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Supermercado no encontrado"
    )

# POST: Crear un nuevo supermercado
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Supermercado)
def supermercado(supermercado: Supermercado): # El cuerpo de la petición (JSON) se convierte automáticamente a objeto Supermercado
    
    # 1. Asignar el ID (Regla de la API)
    supermercado.id = next_id()
    
    # 2. Persistir el dato (añadir a la lista simulada de DB)
    lista_supermercados.append(supermercado)
    
    # 3. Retornar el objeto recién creado (incluyendo el ID) con código 201 Created
    return supermercado


# PUT: Actualizar un supermercado (Reemplazo completo)
@router.put("/{id}", response_model=Supermercado)
def supermercado(id: int, supermercado: Supermercado): # Recibe el ID de la URL y el objeto a actualizar en el cuerpo
    
    # Usamos enumerate para obtener tanto el índice (para actualizar la lista) como el objeto
    for index, supermercado_guardado in enumerate(lista_supermercados):
        if supermercado_guardado.id == id:
            
            # 1. Asegurar que el objeto entrante tenga el ID correcto del path
            supermercado.id = id
            
            # 2. Reemplazar el objeto en el índice de la lista
            lista_supermercados[index] = supermercado
            
            # 3. Retornar el objeto actualizado
            return supermercado
            
    # Si el bucle termina sin encontrar el ID, lanza la excepción 404
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Supermercado no encontrado"
    )


# DELETE: Eliminar un supermercado
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def supermercado(id: int):
    
    # Itera sobre la lista para buscar el supermercado a eliminar
    for supermercado_guardado in lista_supermercados:
        if supermercado_guardado.id == id:
            
            # 1. Eliminar el objeto de la lista (simulación de borrado en DB)
            lista_supermercados.remove(supermercado_guardado)
            
            # 2. Retorna (implícitamente None). El código 204 indica éxito sin contenido en la respuesta.
            return {} # Se retorna {} para una respuesta JSON válida, aunque el status 204 es preferido sin cuerpo.

    # Si el bucle termina sin encontrar el ID, lanza la excepción 404
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Supermercado no encontrado"
    )