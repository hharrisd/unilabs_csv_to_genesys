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


csv_data_personal = """ID_Personal,ID_Estado,Sexo,ID_EstadoCivil,FechaNacimiento,ID_Pais,NacimientoDistrito,DomicilioDistrito,DomicilioTipoVia,DomicilioDireccion,DomicilioNumero,DomicilioInterior,DomicilioTipoZona,DomicilioZona,DomicilioReferencia,DomicilioTelefono,UBIGEO,ID_TipoProfesion,NroColegiatura,ID_Sede,ID_Cargo,ID_CargoTipo,ID_CCosto,ID_UnidadGestion,ID_UnidadProyecto,ID_TipoTrabajador,ID_TipoPersonal,ID_Area,ID_Planilla,ID_Situacion,ID_Horario,FechaIngreso,FechaCese,ID_BcoPagoSueldo,NroCtaPagoSueldo,NroCtaPagoSueldoCCI,TipoCtaPagoSueldo,MonedaPagoSueldo,ID_BcoPagoCTS,NroCtaPagoCTS,NroCtaPagoCTSCCI,TipoCtaPagoCTS,MonedaPagoCTS,CUSPP,Observaciones,AfectoSCRT,ID_TipoNivelEducativo,ID_Categoria,ID_TipoPension,Email
44410897,1,0,,04/03/2024,20,99,0,106,"Jr. General Cordova Nro: 2478 Int: 801 Zona: ","",,99,,,,,,,125,1378,0,,,1301,1,1,3,1,99,,01/02/2024,,,,,,,,,,,,,,0,,1,1,"""

expected_data_personal = [
    {
        "id_personal": 44410897,
        "id_estado": 1,
        "sexo": 0,
        "id_estado_civil": None,
        "fecha_nacimiento": date(2024, 3, 4),
        "id_pais": 20,
        "nacimiento_distrito": 99,
        "domicilio_distrito": 0,
        "domicilio_tipo_via": 106,
        "domicilio_direccion": "Jr. General Cordova Nro: 2478 Int: 801 Zona: ",
        "domicilio_numero": "",
        "domicilio_interior": "",
        "domicilio_tipo_zona": 99,
        "domicilio_zona": "",
        "domicilio_referencia": "",
        "domicilio_telefono": "",
        "ubigeo": "",
        "id_tipo_profesion": None,
        "nro_colegiatura": "",
        "id_sede": 125,
        "id_cargo": 1378,
        "id_cargo_tipo": 0,
        "id_c_costo": None,
        "id_unidad_gestion": None,
        "id_unidad_proyecto": 1301,
        "id_tipo_trabajador": 1,
        "id_tipo_personal": 1,
        "id_area": 3,
        "id_planilla": 1,
        "id_situacion": 99,
        "id_horario": None,
        "fecha_ingreso": date(2024, 2, 1),
        "fecha_cese": None,
        "id_bco_pago_sueldo": None,
        "nro_cta_pago_sueldo": "",
        "nro_cta_pago_sueldo_cci": "",
        "tipo_cta_pago_sueldo": "",
        "moneda_pago_sueldo": "",
        "id_bco_pago_cts": None,
        "nro_cta_pago_cts": "",
        "nro_cta_pago_cts_cci": "",
        "tipo_cta_pago_cts": "",
        "moneda_pago_cts": "",
        "cuspp": "",
        "observaciones": "",
        "afecto_scrt": 0,
        "id_tipo_nivel_educativo": None,
        "id_categoria": 1,
        "id_tipo_pension": 1,
        "email": None,
    }
]
