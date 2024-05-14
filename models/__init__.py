from typing import Type

from pydantic import ValidationError

from .personal import Personal
from .base_csv_model import BaseCSVModel
from .vacacion import Vacacion
from .falta import Falta
from .rrhh_falta import Tmp_RRHHFalta
from .persona_natural import PersonaNatural
from .autorizar_h_e import AutorizarHE
from .concepto_aplicado import ConceptoAplicado
from .dato_extra import DatoExtra
from .licencia import Licencia

model_mapper = {
    '_TMP_RRHHFalta_': {'pydantic_model': Falta, 'orm_model': Tmp_RRHHFalta}
}


def csv_load(data: list, table: str):
    """
    Utility function to load data into model instances from CSV data.
    :param data:
    :param table:
    :return:
    """
    model = model_mapper[table]['pydantic_model']

    try:
        model_data_list = [model.from_csv_row(line) for line in data[1:]]
    except ValidationError as e:
        print(f"Error al parsear los datos CSV: {e}")

    return model_data_list
