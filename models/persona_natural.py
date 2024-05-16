from typing import Optional

from models.base_models import BaseCSVModel


class PersonaNatural(BaseCSVModel):
    Nombre1: str
    Nombre2: Optional[str] = None
    ApellidoPaterno: str
    ApellidoMaterno: Optional[str] = None
    DNI: str
    RUC: Optional[str] = None
