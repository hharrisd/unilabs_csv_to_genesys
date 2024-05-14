from datetime import date, datetime
from typing import Optional

from pydantic import field_validator

from models.base_csv_model import BaseCSVModel


class Falta(BaseCSVModel):
    ID_Personal: str
    Fecha: datetime
    ID_TipoFalta: int
    Descripcion: Optional[str] = None
    Estado: int
    Condicion: int
    Cantidad_Horas: int
    Observaciones: Optional[str] = None

    @field_validator('Fecha', mode='before')
    def validate_fecha(cls, value):
        return super().validate_fecha(value)
