from datetime import date
from typing import Optional

from pydantic import field_validator

from models.base_models import BaseCSVModel


class DatoExtra(BaseCSVModel):
    ID_Personal: str
    ID_TipoFileDatoExtra: int
    Fecha: date
    ID_Moneda: int
    Importe: float
    Observaciones: Optional[str] = None
    ID_PlanillaConf: Optional[int] = None

    @field_validator('Fecha', mode='before')
    def validate_fecha(cls, value):
        return super().validate_fecha(value)
