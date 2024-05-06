from datetime import date
from typing import Optional

from pydantic import field_validator

from models.base_csv_model import BaseCSVModel


class Licencia(BaseCSVModel):
    id_personal: str
    fecha: date
    id_tipo_licencia: int
    descripcion: str
    estado: int
    condicion: int
    solicitado_horas: float
    observaciones: Optional[str] = None
    id_tipo_enfermedad: Optional[int] = None
    id_tipo_accidente_trabajo: Optional[int] = None
    id_tipo_parte_lesionada: Optional[int] = None
    id_tipo_naturaleza_lesion: Optional[int] = None
    id_tipo_maternidad: Optional[int] = None
    id_tipo_aplicacion_licencia: Optional[int] = None

    @field_validator('fecha', mode='before')
    def validate_fecha(cls, value):
        return super().validate_fecha(value)
