from datetime import date

csv_str = """ID_Personal,ID_TipoConcepto,Vigencia,ID_Moneda,Monto,Observaciones
12345,1,01/06/2023,1,100.50,
67890,2,01/07/2023,2,200.75,Concepto especial
24680,3,01/08/2023,1,150.25,
13579,4,01/09/2023,2,175.00,"""

expected_list = [
    {
        'id_personal': '12345',
        'id_tipo_concepto': 1,
        'vigencia': date(2023, 6, 1),
        'id_moneda': 1,
        'monto': 100.50,
        'observaciones': None,
    },
    {
        'id_personal': '67890',
        'id_tipo_concepto': 2,
        'vigencia': date(2023, 7, 1),
        'id_moneda': 2,
        'monto': 200.75,
        'observaciones': 'Concepto especial',
    },
    {
        'id_personal': '24680',
        'id_tipo_concepto': 3,
        'vigencia': date(2023, 8, 1),
        'id_moneda': 1,
        'monto': 150.25,
        'observaciones': None,
    },
    {
        'id_personal': '13579',
        'id_tipo_concepto': 4,
        'vigencia': date(2023, 9, 1),
        'id_moneda': 2,
        'monto': 175.00,
        'observaciones': None,
    },
]
