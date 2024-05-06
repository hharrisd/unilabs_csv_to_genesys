csv_str = """Nombre1,Nombre2,ApellidoPaterno,ApellidoMaterno,DNI,RUC
Alejandro,,Benavides,Samame,10109403,
María,Elizabeth,Rodríguez,López,87654321,20123456789
Pedro,,García,Martínez,98765432,
Juan,Carlos,Pérez,González,12345678,"""

expected_list = [
    {
        'nombre1': 'Alejandro',
        'nombre2': None,
        'apellido_paterno': 'Benavides',
        'apellido_materno': 'Samame',
        'dni': '10109403',
        'ruc': None,
    },
    {
        'nombre1': 'María',
        'nombre2': 'Elizabeth',
        'apellido_paterno': 'Rodríguez',
        'apellido_materno': 'López',
        'dni': '87654321',
        'ruc': '20123456789',
    },
    {
        'nombre1': 'Pedro',
        'nombre2': None,
        'apellido_paterno': 'García',
        'apellido_materno': 'Martínez',
        'dni': '98765432',
        'ruc': None,
    },
    {
        'nombre1': 'Juan',
        'nombre2': 'Carlos',
        'apellido_paterno': 'Pérez',
        'apellido_materno': 'González',
        'dni': '12345678',
        'ruc': None,
    },
]
