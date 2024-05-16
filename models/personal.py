from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, field_validator

from .base_models import BaseCSVModel


class Personal(BaseCSVModel):
    ID_Personal: str
    ID_Estado: int
    Sexo: str
    ID_EstadoCivil: int
    FechaNacimiento: date
    ID_Pais: int
    NacimientoDistrito: int
    DomicilioDistrito: int
    DomicilioTipoVia: int
    DomicilioDireccion: Optional[str] = None
    DomicilioNumero: Optional[str] = None
    DomicilioInterior: Optional[str] = None
    DomicilioTipoZona: Optional[int] = None
    DomicilioZona: Optional[str] = None
    DomicilioReferencia: Optional[str] = None
    DomicilioTelefono: Optional[str] = None
    UBIGEO: Optional[str] = None
    ID_TipoProfesion: int
    NroColegiatura: Optional[str] = None
    ID_Sede: int
    ID_Cargo: int
    ID_CargoTipo: int
    ID_CCosto: Optional[str] = None
    ID_UnidadGestion: Optional[str] = None
    ID_UnidadProyecto: Optional[str] = None
    ID_TipoTrabajador: int
    ID_TipoPersonal: int
    ID_Area: int
    ID_Planilla: int
    ID_Situacion: int
    ID_Horario: int
    FechaIngreso: date
    FechaCese: Optional[date] = None
    ID_BcoPagoSueldo: Optional[str] = None
    NroCtaPagoSueldo: Optional[str] = None
    NroCtaPagoSueldoCCI: Optional[str] = None
    TipoCtaPagoSueldo: Optional[int] = None
    MonedaPagoSueldo: Optional[int] = None
    ID_BcoPagoCTS: Optional[str] = None
    NroCtaPagoCTS: Optional[str] = None
    NroCtaPagoCTSCCI: Optional[str] = None
    TipoCtaPagoCTS: Optional[int] = None
    MonedaPagoCTS: Optional[int] = None
    CUSPP: Optional[str] = None
    Observaciones: Optional[str] = None
    AfectoSCRT: int
    ID_TipoNivelEducativo: Optional[int] = None
    ID_Categoria: Optional[int] = None
    ID_TipoPension: Optional[int] = None
    Email: Optional[str] = None

    @field_validator('FechaNacimiento', mode='before')
    def validate_fecha_nacimiento(cls, value):
        return super().validate_fecha(value)

    @field_validator('FechaIngreso', mode='before')
    def validate_fecha_ingreso(cls, value):
        return super().validate_fecha(value)

    @field_validator('FechaCese', mode='before')
    def validate_fecha_cese(cls, value):
        return super().validate_fecha(value)
