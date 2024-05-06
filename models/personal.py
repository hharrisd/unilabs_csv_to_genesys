from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, field_validator

from .base_csv_model import BaseCSVModel


class Personal(BaseCSVModel):
    id_personal: str
    id_estado: int
    sexo: str
    id_estado_civil: int
    fecha_nacimiento: date
    id_pais: int
    nacimiento_distrito: int
    domicilio_distrito: int
    domicilio_tipo_via: int
    domicilio_direccion: Optional[str] = None
    domicilio_numero: Optional[str] = None
    domicilio_interior: Optional[str] = None
    domicilio_tipo_zona: Optional[int] = None
    domicilio_zona: Optional[str] = None
    domicilio_referencia: Optional[str] = None
    domicilio_telefono: Optional[str] = None
    ubigeo: Optional[str] = None
    id_tipo_profesion: int
    nro_colegiatura: Optional[str] = None
    id_sede: int
    id_cargo: int
    id_cargo_tipo: int
    id_c_costo: Optional[str] = None
    id_unidad_gestion: Optional[str] = None
    id_unidad_proyecto: Optional[str] = None
    id_tipo_trabajador: int
    id_tipo_personal: int
    id_area: int
    id_planilla: int
    id_situacion: int
    id_horario: int
    fecha_ingreso: date
    fecha_cese: Optional[date] = None
    id_bco_pago_sueldo: Optional[str] = None
    nro_cta_pago_sueldo: Optional[str] = None
    nro_cta_pago_sueldo_cci: Optional[str] = None
    tipo_cta_pago_sueldo: Optional[int] = None
    moneda_pago_sueldo: Optional[int] = None
    id_bco_pago_cts: Optional[str] = None
    nro_cta_pago_cts: Optional[str] = None
    nro_cta_pago_cts_cci: Optional[str] = None
    tipo_cta_pago_cts: Optional[int] = None
    moneda_pago_cts: Optional[int] = None
    cuspp: Optional[str] = None
    observaciones: Optional[str] = None
    afecto_scrt: int
    id_tipo_nivel_educativo: Optional[int] = None
    id_categoria: Optional[int] = None
    id_tipo_pension: Optional[int] = None
    email: Optional[str] = None

    @field_validator('fecha_nacimiento', mode='before')
    def validate_fecha_nacimiento(cls, value):
        return super().validate_fecha(value)

    @field_validator('fecha_ingreso', mode='before')
    def validate_fecha_ingreso(cls, value):
        return super().validate_fecha(value)

    @field_validator('fecha_cese', mode='before')
    def validate_fecha_cese(cls, value):
        return super().validate_fecha(value)
