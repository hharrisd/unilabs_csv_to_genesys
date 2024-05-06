from datetime import date
from typing import Optional

from pydantic import field_validator

from models.base_csv_model import BaseCSVModel


class ConceptoAplicado(BaseCSVModel):
    id_personal: str
    id_tipo_concepto: int
    vigencia: date
    id_moneda: int
    monto: float
    observaciones: Optional[str] = None

    @field_validator('vigencia', mode='before')
    def validate_vigencia(cls, value):
        return super().validate_fecha(value)
