from datetime import date
from typing import Optional

from pydantic import field_validator

from .base_models import BaseCSVModel


class Vacacion(BaseCSVModel):
    ID_Personal: str
    Fecha: date
    Cantidad_Horas: int
    PeriodoAño: int
    Observaciones: Optional[str] = None

    @field_validator('Fecha', mode='before')
    def validate_fecha(cls, value):
        return super().validate_fecha(value)
