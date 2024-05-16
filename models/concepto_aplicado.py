from datetime import date
from typing import Optional

from pydantic import field_validator

from models.base_models import BaseCSVModel


class ConceptoAplicado(BaseCSVModel):
    ID_Personal: str
    ID_TipoConcepto: int
    Vigencia: date
    ID_Moneda: int
    Monto: float
    Observaciones: Optional[str] = None

    @field_validator('Vigencia', mode='before')
    def validate_vigencia(cls, value):
        return super().validate_fecha(value)
