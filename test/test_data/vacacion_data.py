from datetime import date

csv_str = """ID_Personal,Fecha,Cantidad_Horas,PeriodoAño,Observaciones
40770860,04/03/2024,0,2024,"""

expected_list = [
    {
        'id_personal': '40770860',
        'fecha': date(2024, 3, 4),
        'cantidad_horas': 0,
        'periodo_ano': 2024,
        'observaciones': None
    }
]
