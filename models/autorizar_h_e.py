from datetime import date
from typing import Optional

from pydantic import field_validator

from models.base_models import BaseCSVModel


class AutorizarHE(BaseCSVModel):
    ID_Personal: str
    Fecha: date
    HoraInicio: float
    HoraTermino: float
    HorasExtras_Autorizadas: float

    @field_validator('Fecha', mode='before')
    def validate_fecha(cls, value):
        return super().validate_fecha(value)
