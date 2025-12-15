from typing import Optional
from pydantic import BaseModel

# Entidad colegio
class Colegio(BaseModel):
    Id: str
    Nombre: str
    Distrito: str
    Tipo: str
    Direccion: str