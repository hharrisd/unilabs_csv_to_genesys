from datetime import datetime

csv_str = """ID_Personal,ID_Estado,Sexo,ID_EstadoCivil,FechaNacimiento,ID_Pais,NacimientoDistrito,DomicilioDistrito,DomicilioTipoVia,DomicilioDireccion,DomicilioNumero,DomicilioInterior,DomicilioTipoZona,DomicilioZona,DomicilioReferencia,DomicilioTelefono,UBIGEO,ID_TipoProfesion,NroColegiatura,ID_Sede,ID_Cargo,ID_CargoTipo,ID_CCosto,ID_UnidadGestion,ID_UnidadProyecto,ID_TipoTrabajador,ID_TipoPersonal,ID_Area,ID_Planilla,ID_Situacion,ID_Horario,FechaIngreso,FechaCese,ID_BcoPagoSueldo,NroCtaPagoSueldo,NroCtaPagoSueldoCCI,TipoCtaPagoSueldo,MonedaPagoSueldo,ID_BcoPagoCTS,NroCtaPagoCTS,NroCtaPagoCTSCCI,TipoCtaPagoCTS,MonedaPagoCTS,CUSPP,Observaciones,AfectoSCRT,ID_TipoNivelEducativo,ID_Categoria,ID_TipoPension,Email
44410897,1,0,1,16/06/1987,20,99,0,106,"Jr. General Cordova Nro: 2478 Int: 801 Zona: ",,,99,,,,,1,,125,1378,0,,,1301,1,1,3,1,99,1,01/02/2024,,,,,,,,,,,,,,0,,1,1,"""

expected_list = [
    {
        "ID_Personal": '44410897',
        "ID_Estado": 1,
        "Sexo": '0',
        "ID_EstadoCivil": 1,
        "FechaNacimiento": datetime(1987, 6, 16),
        "ID_Pais": 20,
        "NacimientoDistrito": 99,
        "DomicilioDistrito": 0,
        "DomicilioTipoVia": 106,
        "DomicilioDireccion": "Jr. General Cordova Nro: 2478 Int: 801 Zona: ",
        "DomicilioNumero": None,
        "DomicilioInterior": None,
        "DomicilioTipoZona": 99,
        "DomicilioZona": None,
        "DomicilioReferencia": None,
        "DomicilioTelefono": None,
        "UBIGEO": None,
        "ID_TipoProfesion": 1,
        "NroColegiatura": None,
        "ID_Sede": 125,
        "ID_Cargo": 1378,
        "ID_CargoTipo": 0,
        "ID_CCosto": None,
        "ID_UnidadGestion": None,
        "ID_UnidadProyecto": '1301',
        "ID_TipoTrabajador": 1,
        "ID_TipoPersonal": 1,
        "ID_Area": 3,
        "ID_Planilla": 1,
        "ID_Situacion": 99,
        "ID_Horario": 1,
        "FechaIngreso": datetime(2024, 2, 1),
        "FechaCese": None,
        "ID_BcoPagoSueldo": None,
        "NroCtaPagoSueldo": None,
        "NroCtaPagoSueldoCCI": None,
        "TipoCtaPagoSueldo": None,
        "MonedaPagoSueldo": None,
        "ID_BcoPagoCTS": None,
        "NroCtaPagoCTS": None,
        "NroCtaPagoCTSCCI": None,
        "TipoCtaPagoCTS": 4,
        "MonedaPagoCTS": None,
        "CUSPP": None,
        "Observaciones": None,
        "AfectoSCRT": 0,
        "ID_TipoNivelEducativo": None,
        "ID_Categoria": 1,
        "ID_TipoPension": 1,
        "Email": None,
    }
]
