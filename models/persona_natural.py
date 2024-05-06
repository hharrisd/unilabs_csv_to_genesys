from typing import Optional

from models.base_csv_model import BaseCSVModel


class PersonaNatural(BaseCSVModel):
    nombre1: str
    nombre2: Optional[str] = None
    apellido_paterno: str
    apellido_materno: Optional[str] = None
    dni: str
    ruc: Optional[str] = None
