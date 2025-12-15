from typing import Optional
from pydantic import BaseModel

# Entidad alumno
class Alumno(BaseModel):
    Id: str
    Nombre: str
    Apellidos: str
    Fecha_Nac: str
    Curso: str
    Repetidor: bool
    id_colegio: str