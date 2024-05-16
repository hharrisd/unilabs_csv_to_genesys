from datetime import date
from typing import Optional

from pydantic import field_validator

from models.base_models import BaseCSVModel


class Licencia(BaseCSVModel):
    ID_Personal: str
    Fecha: date
    ID_TipoLicencia: int
    Descripcion: str
    Estado: int
    Condicion: int
    Solicitado_Horas: float
    Observaciones: Optional[str] = None
    ID_TipoEnfermedad: Optional[int] = None
    ID_TipoAccidenteTrabajo: Optional[int] = None
    ID_TipoParteLesionada: Optional[int] = None
    ID_TipoNaturalezaLesion: Optional[int] = None
    ID_TipoMaternidad: Optional[int] = None
    ID_TipoAplicacionLicencia: Optional[int] = None

    @field_validator('Fecha', mode='before')
    def validate_fecha(cls, value):
        return super().validate_fecha(value)
