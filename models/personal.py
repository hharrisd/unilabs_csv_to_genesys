from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from pydantic import field_validator
from sqlalchemy import String, DateTime, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from models.base_models import BaseCSVModel, BaseORM, BaseModelFactory


class Personal(BaseCSVModel):
    ID_Personal: str
    ID_Estado: int
    Sexo: str
    ID_EstadoCivil: int
    FechaNacimiento: datetime
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
    FechaIngreso: datetime
    FechaCese: Optional[datetime] = None
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


class PersonalEntity(BaseORM):
    __tablename__ = 'TMP_RRHHPersonal'

    Op: Mapped[int] = mapped_column(Numeric(18, 0), primary_key=True, autoincrement=True)
    ID_Personal: Mapped[str] = mapped_column(String(20), nullable=False)
    ID_Estado: Mapped[int] = mapped_column(Integer, nullable=False)
    Sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    ID_EstadoCivil: Mapped[int] = mapped_column(Integer, nullable=False)
    FechaNacimiento: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    ID_Pais: Mapped[int] = mapped_column(Numeric(18, 0), nullable=False)
    NacimientoDistrito: Mapped[int] = mapped_column(Numeric(18, 0), nullable=False)
    DomicilioDistrito: Mapped[int] = mapped_column(Numeric(18, 0), nullable=False)
    DomicilioTipoVia: Mapped[int] = mapped_column(Integer, nullable=False)
    DomicilioDireccion: Mapped[str] = mapped_column(String(50), nullable=True)
    DomicilioNumero: Mapped[str] = mapped_column(String(20), nullable=True)
    DomicilioInterior: Mapped[str] = mapped_column(String(20), nullable=True)
    DomicilioTipoZona: Mapped[int] = mapped_column(Integer, nullable=True)
    DomicilioZona: Mapped[str] = mapped_column(String(50), nullable=True)
    DomicilioReferencia: Mapped[str] = mapped_column(String(50), nullable=True)
    DomicilioTelefono: Mapped[str] = mapped_column(String(20), nullable=True)
    UBIGEO: Mapped[str] = mapped_column(String(10), nullable=True)
    ID_TipoProfesion: Mapped[int] = mapped_column(Integer, nullable=False)
    NroColegiatura: Mapped[str] = mapped_column(String(20), nullable=True)
    ID_Sede: Mapped[int] = mapped_column(Integer, nullable=False)
    ID_Cargo: Mapped[int] = mapped_column(Integer, nullable=False)
    ID_CargoTipo: Mapped[int] = mapped_column(Integer, nullable=False)
    ID_CCosto: Mapped[str] = mapped_column(String(12), nullable=True)
    ID_UnidadGestion: Mapped[str] = mapped_column(String(12), nullable=True)
    ID_UnidadProyecto: Mapped[str] = mapped_column(String(12), nullable=True)
    ID_TipoTrabajador: Mapped[int] = mapped_column(Integer, nullable=False)
    ID_TipoPersonal: Mapped[int] = mapped_column(Integer, nullable=False)
    ID_Area: Mapped[int] = mapped_column(Numeric(18, 0), nullable=False)
    ID_Planilla: Mapped[int] = mapped_column(Numeric(18, 0), nullable=False)
    ID_Situacion: Mapped[int] = mapped_column(Integer, nullable=False)
    ID_Horario: Mapped[int] = mapped_column(Integer, nullable=False)
    FechaIngreso: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    FechaCese: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    ID_BcoPagoSueldo: Mapped[str] = mapped_column(String(20), nullable=True)
    NroCtaPagoSueldo: Mapped[str] = mapped_column(String(20), nullable=True)
    NroCtaPagoSueldoCCI: Mapped[str] = mapped_column(String(20), nullable=True)
    TipoCtaPagoSueldo: Mapped[int] = mapped_column(Integer, nullable=True)
    MonedaPagoSueldo: Mapped[int] = mapped_column(Numeric(18, 0), nullable=True)
    ID_BcoPagoCTS: Mapped[str] = mapped_column(String(20), nullable=True)
    NroCtaPagoCTS: Mapped[str] = mapped_column(String(20), nullable=True)
    NroCtaPagoCTSCCI: Mapped[str] = mapped_column(String(20), nullable=True)
    TipoCtaPagoCTS: Mapped[int] = mapped_column(Integer, nullable=True)
    MonedaPagoCTS: Mapped[int] = mapped_column(Numeric(18, 0), nullable=True)
    CUSPP: Mapped[str] = mapped_column(String(50), nullable=True)
    Observaciones: Mapped[str] = mapped_column(String(50), nullable=True)
    AfectoSCRT: Mapped[int] = mapped_column(Integer, nullable=False)
    ID_TipoNivelEducativo: Mapped[int] = mapped_column(Integer, nullable=True)
    ID_Categoria: Mapped[int] = mapped_column(Integer, nullable=True)
    ID_TipoPension: Mapped[int] = mapped_column(Integer, nullable=True)
    Email: Mapped[str] = mapped_column(String(255), nullable=True)

    def __repr__(self):
        return (
            f"TMP_RRHHPersonal(ID_Personal='{self.ID_Personal}', ID_Estado={self.ID_Estado}, Sexo='{self.Sexo}', "
            f"ID_EstadoCivil={self.ID_EstadoCivil}, FechaNacimiento='{self.FechaNacimiento}', ID_Pais={self.ID_Pais}, "
            f"NacimientoDistrito={self.NacimientoDistrito}, DomicilioDistrito={self.DomicilioDistrito}, "
            f"DomicilioTipoVia={self.DomicilioTipoVia}, DomicilioDireccion='{self.DomicilioDireccion}', "
            f"DomicilioNumero='{self.DomicilioNumero}', DomicilioInterior='{self.DomicilioInterior}', "
            f"DomicilioTipoZona={self.DomicilioTipoZona}, DomicilioZona='{self.DomicilioZona}', "
            f"DomicilioReferencia='{self.DomicilioReferencia}', DomicilioTelefono='{self.DomicilioTelefono}', "
            f"UBIGEO='{self.UBIGEO}', ID_TipoProfesion={self.ID_TipoProfesion}, NroColegiatura='{self.NroColegiatura}', "
            f"ID_Sede={self.ID_Sede}, ID_Cargo={self.ID_Cargo}, ID_CargoTipo={self.ID_CargoTipo}, "
            f"ID_CCosto='{self.ID_CCosto}', ID_UnidadGestion='{self.ID_UnidadGestion}', "
            f"ID_UnidadProyecto='{self.ID_UnidadProyecto}', ID_TipoTrabajador={self.ID_TipoTrabajador}, "
            f"ID_TipoPersonal={self.ID_TipoPersonal}, ID_Area={self.ID_Area}, ID_Planilla={self.ID_Planilla}, "
            f"ID_Situacion={self.ID_Situacion}, ID_Horario={self.ID_Horario}, FechaIngreso='{self.FechaIngreso}', "
            f"FechaCese='{self.FechaCese}', ID_BcoPagoSueldo='{self.ID_BcoPagoSueldo}', "
            f"NroCtaPagoSueldo='{self.NroCtaPagoSueldo}', NroCtaPagoSueldoCCI='{self.NroCtaPagoSueldoCCI}', "
            f"TipoCtaPagoSueldo={self.TipoCtaPagoSueldo}, MonedaPagoSueldo={self.MonedaPagoSueldo}, "
            f"ID_BcoPagoCTS='{self.ID_BcoPagoCTS}', NroCtaPagoCTS='{self.NroCtaPagoCTS}', "
            f"NroCtaPagoCTSCCI='{self.NroCtaPagoCTSCCI}', TipoCtaPagoCTS={self.TipoCtaPagoCTS}, "
            f"MonedaPagoCTS={self.MonedaPagoCTS}, CUSPP='{self.CUSPP}', Observaciones='{self.Observaciones}', "
            f"AfectoSCRT={self.AfectoSCRT}, ID_TipoNivelEducativo={self.ID_TipoNivelEducativo}, "
            f"ID_Categoria={self.ID_Categoria}, ID_TipoPension={self.ID_TipoPension}, Email='{self.Email}')"
        )


@dataclass
class PersonalFactory(BaseModelFactory):
    pydantic_model = Personal
    orm_model = PersonalEntity
    procedures = [('EXEC sp_TMPRRHHPersonal', None)]
