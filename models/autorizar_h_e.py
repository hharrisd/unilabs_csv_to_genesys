from datetime import date
from typing import Optional

from pydantic import field_validator

from models.base_csv_model import BaseCSVModel


class AutorizarHE(BaseCSVModel):
    id_personal: str
    fecha: date
    hora_inicio: float
    hora_termino: float
    horas_extras_autorizadas: float

    @field_validator('fecha', mode='before')
    def validate_fecha(cls, value):
        return super().validate_fecha(value)
