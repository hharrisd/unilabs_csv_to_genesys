from datetime import date

csv_str= """ID_Personal,Fecha,HoraInicio,HoraTermino,HorasExtras_Autorizadas
12345,01/05/2023,8.5,17.5,9
67890,02/05/2023,9.0,18.0,9
24680,03/05/2023,7.5,16.5,9
13579,04/05/2023,10.0,19.0,9"""

expected_list = [
    {
        'id_personal': '12345',
        'fecha': date(2023, 5, 1),
        'hora_inicio': 8.5,
        'hora_termino': 17.5,
        'horas_extras_autorizadas': 9.0,
    },
    {
        'id_personal': '67890',
        'fecha': date(2023, 5, 2),
        'hora_inicio': 9.0,
        'hora_termino': 18.0,
        'horas_extras_autorizadas': 9.0,
    },
    {
        'id_personal': '24680',
        'fecha': date(2023, 5, 3),
        'hora_inicio': 7.5,
        'hora_termino': 16.5,
        'horas_extras_autorizadas': 9.0,
    },
    {
        'id_personal': '13579',
        'fecha': date(2023, 5, 4),
        'hora_inicio': 10.0,
        'hora_termino': 19.0,
        'horas_extras_autorizadas': 9.0,
    },
]
