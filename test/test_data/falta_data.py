from datetime import date

csv_str = """ID_Personal,Fecha,ID_TipoFalta,Descripcion,Estado,Condicion,Cantidad_Horas,observaciones
09330594,09/02/2024,4,,1,0,2
43090510,30/01/2024,1,,1,1,1
43090510,02/01/2024,1,,1,1,1
09993871,16/01/2024,1,,1,1,1
09993871,31/01/2024,1,,1,1,1
42860009,23/01/2024,1,,1,1,1
47428300,18/01/2024,1,,1,1,1
47428300,05/02/2024,1,,1,1,1,Ejemplo de observaciones
"""

expected_list = [
    {
        "id_personal": '09330594',
        "fecha": date(2024, 2, 9),
        "id_tipo_falta": 4,
        "descripcion": None,
        "estado": 1,
        "condicion": 0,
        "cantidad_horas": 2,
    },
    {
        "id_personal": '43090510',
        "fecha": date(2024, 1, 30),
        "id_tipo_falta": 1,
        "descripcion": None,
        "estado": 1,
        "condicion": 1,
        "cantidad_horas": 1,
    },
    {
        "id_personal": '43090510',
        "fecha": date(2024, 1, 2),
        "id_tipo_falta": 1,
        "descripcion": None,
        "estado": 1,
        "condicion": 1,
        "cantidad_horas": 1,
    },
    {
        "id_personal": '09993871',
        "fecha": date(2024, 1, 16),
        "id_tipo_falta": 1,
        "descripcion": None,
        "estado": 1,
        "condicion": 1,
        "cantidad_horas": 1,
    },
    {
        "id_personal": '09993871',
        "fecha": date(2024, 1, 31),
        "id_tipo_falta": 1,
        "descripcion": None,
        "estado": 1,
        "condicion": 1,
        "cantidad_horas": 1,
    },
    {
        "id_personal": '42860009',
        "fecha": date(2024, 1, 23),
        "id_tipo_falta": 1,
        "descripcion": None,
        "estado": 1,
        "condicion": 1,
        "cantidad_horas": 1,
    },
    {
        "id_personal": '47428300',
        "fecha": date(2024, 1, 18),
        "id_tipo_falta": 1,
        "descripcion": None,
        "estado": 1,
        "condicion": 1,
        "cantidad_horas": 1,
    },
    {
        "id_personal": '47428300',
        "fecha": date(2024, 2, 5),
        "id_tipo_falta": 1,
        "descripcion": None,
        "estado": 1,
        "condicion": 1,
        "cantidad_horas": 1,
        'observaciones': 'Ejemplo de observaciones'
    },
]
