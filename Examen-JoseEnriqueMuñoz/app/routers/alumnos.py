from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.schemas.alumno import alumno_schema, alumnos_schema
from db.schemas.colegio import colegio_schema, colegios_schema
from db.models.alumno import Alumno
from db.models.colegio import Colegio

router = APIRouter(prefix="/alumnos", tags=["alumnos"])

class Alumno(BaseModel):
    Id: str
    Nombre: str
    Apellidos: str
    Fecha_Nac: str
    Curso: str
    Repetidor: bool
    id_colegio: str


lista_alumnos = [
    {"Id": "1", "Nombre": "Fernando", "Apellidos": "Ruiz Morales", "Fecha_Nac": "18-12-2001", "Curso": "1ESO", "Repetidor": False, "id_colegio": "1"},
    {"Id": "2", "Nombre": "Juan", "Apellidos": "Ruiz Perez", "Fecha_Nac": "19-12-2001", "Curso": "1BACH", "Repetidor": True, "id_colegio": "2"},
    {"Id": "3", "Nombre": "Pedro", "Apellidos": "Perez Morales", "Fecha_Nac": "19-12-2001", "Curso": "2ESO", "Repetidor": False, "id_colegio": "3"},
]

# Función para generar el próximo ID. Necesaria porque la lista no lo hace automáticamente.
def next_id():
    if not lista_alumnos:
        return 1
    # Encuentra el ID más alto y suma 1. (NOTA: Esto fallará si 'lista_alumnos' sigue siendo una lista de diccionarios 
    # y la lógica intenta acceder a 'a.id' en lugar de 'a["Id"]').
    return max(a.id for a in lista_alumnos) + 1

# GET: Obtener todos los alumnos (Ruta raíz del router)
@router.get("/")
def obtener_directorres():
    # Retorna la lista de diccionarios. FastAPI lo convierte a JSON automáticamente.
    return lista_alumnos


# GET: Obtener un alumno por ID (Parámetro de Ruta)
@router.get("/colegio/{alumno_id}", response_model=Alumno)
def obtener_alumno(alumno_id: int): # 'alumno_id' se extrae de la URL 
    # Itera sobre la lista simulada
    for a in lista_alumnos:

        if (Alumno.id_Colegio == Colegio.Id):

            # Compara el Id del dato guardado con el ID solicitado
            if a["Id"] == alumno_id: 
                return a # Retorna el diccionario encontrado
        
        else: 

            # Si no se encuentra, lanza una excepción HTTP con código 404 (No encontrado)
            raise HTTPException(status_code=404, detail="Colegio no encontrado")
    
    # Si no se encuentra, lanza una excepción HTTP con código 404 (No encontrado)
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

# POST: Crear un nuevo alumno
@router.post("/", status_code=201, response_model=Alumno)
def alumno(alumno: Alumno): # El cuerpo de la petición se valida como un objeto Alumno
    
    # Asigna el ID generado por la función auxiliar
    alumno.Id = next_id()

    #Comprobamos si el curso es correcto
    if (curso_correcto):
    
        # Añade el nuevo objeto Alumno a la lista (persistencia simulada)
        lista_alumnos.append(alumno)

    else:
        
        raise HTTPException(status_code=404, detail="Curso incorrecto")
    
    # Retorna el objeto creado con el nuevo ID (código 201: Creado)
    return alumno


# PUT: Actualizar un alumno (Reemplazo completo)
@router.put("/{id}", response_model=Alumno)
def alumno(id: int, director: Alumno): # 'id' de la URL, 'alumno' del cuerpo de la petición
    
    # Itera sobre la lista usando enumerate para obtener el índice y el valor
    for index, alumno_guardado in enumerate(lista_alumnos):
        # Busca el alumno por ID
        if alumno_guardado.Id == id: 
            
            # Asigna el ID de la URL al objeto entrante para asegurar consistencia
            alumno.Id = id
            
            # Reemplaza el elemento antiguo en la lista con el nuevo objeto
            lista_alumnos[index] = alumno
            
            return alumno # Retorna el alumno actualizado
            
    # Si el ID no se encuentra
    raise HTTPException(status_code=404, detail="Alumno no encontrado")


# DELETE: Eliminar un alumno
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def alumno(id: int):
    
    # Itera sobre la lista para encontrar el alumno a eliminar
    for alumno_guardado in lista_alumnos:
        if alumno_guardado.Id == id:
            # Elimina el objeto de la lista (simulación de borrado)
            lista_alumnos.remove(alumno_guardado)
            
            # Retorna un cuerpo vacío ({}) con código 204 (No Content), indicando éxito
            return {} 
            
    # Si el ID no se encuentra
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

# Funcion para filtrar que el curso sea correcto
def curso_correcto(curso: str):

    existe: bool = False

    if (curso == "1ESO" | curso == "2ESO" | curso == "3ESO" | curso == "4ESO" | curso == "1BACH" | curso == "2BACH" ):

        existe = True

    return existe
