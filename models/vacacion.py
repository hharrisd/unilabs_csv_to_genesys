from datetime import date
from typing import Optional

from pydantic import field_validator

from .base_csv_model import BaseCSVModel


class Vacacion(BaseCSVModel):
    id_personal: str
    fecha: date
    cantidad_horas: int
    periodo_ano: int
    observaciones: Optional[str] = None

    @field_validator('fecha', mode='before')
    def validate_fecha(cls, value):
        return super().validate_fecha(value)
