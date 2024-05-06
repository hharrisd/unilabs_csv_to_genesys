from datetime import date
from typing import Optional

from pydantic import field_validator

from models.base_csv_model import BaseCSVModel


class DatoExtra(BaseCSVModel):
    id_personal: str
    id_tipo_file_dato_extra: int
    fecha: date
    id_moneda: int
    importe: float
    observaciones: Optional[str] = None
    id_planilla_conf: Optional[int] = None

    @field_validator('fecha', mode='before')
    def validate_fecha(cls, value):
        return super().validate_fecha(value)
