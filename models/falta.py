from datetime import date
from typing import Optional

from pydantic import field_validator

from models.base_csv_model import BaseCSVModel


class Falta(BaseCSVModel):
    id_personal: str
    fecha: date
    id_tipo_falta: int
    descripcion: Optional[str] = None
    estado: int
    condicion: int
    cantidad_horas: int
    observaciones: Optional[str] = None

    @field_validator('fecha', mode='before')
    def validate_fecha(cls, value):
        return super().validate_fecha(value)
