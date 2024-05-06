from datetime import date

csv_str = """ID_Personal,ID_TipoFileDatoExtra,Fecha,ID_Moneda,Importe,Observaciones,ID_PlanillaConf
12345,1,01/06/2023,1,100.50,,
67890,2,01/07/2023,2,200.75,Dato especial,1234
24680,3,01/08/2023,1,150.25,,5678
13579,4,01/09/2023,2,175.00,,"""

expected_list = [
    {
        'id_personal': '12345',
        'id_tipo_file_dato_extra': 1,
        'fecha': date(2023, 6, 1),
        'id_moneda': 1,
        'importe': 100.50,
        'observaciones': None,
        'id_planilla_conf': None,
    },
    {
        'id_personal': '67890',
        'id_tipo_file_dato_extra': 2,
        'fecha': date(2023, 7, 1),
        'id_moneda': 2,
        'importe': 200.75,
        'observaciones': 'Dato especial',
        'id_planilla_conf': 1234,
    },
    {
        'id_personal': '24680',
        'id_tipo_file_dato_extra': 3,
        'fecha': date(2023, 8, 1),
        'id_moneda': 1,
        'importe': 150.25,
        'observaciones': None,
        'id_planilla_conf': 5678,
    },
    {
        'id_personal': '13579',
        'id_tipo_file_dato_extra': 4,
        'fecha': date(2023, 9, 1),
        'id_moneda': 2,
        'importe': 175.00,
        'observaciones': None,
        'id_planilla_conf': None,
    },
]
