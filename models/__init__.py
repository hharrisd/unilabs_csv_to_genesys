from logging import Logger
from typing import Type

from pydantic import ValidationError

from .autorizar_h_e import AutorizarHE
from .base_models import BaseCSVModel, BaseModelFactory
from .concepto_aplicado import ConceptoAplicado
from .dato_extra import DatoExtra
from .falta import Falta, FaltaFactory
from .licencia import Licencia
from .persona_natural import PersonaNatural
from .personal import Personal
from .vacacion import Vacacion


model_mapper: dict[str, Type[BaseModelFactory]] = {
    '_TMP_RRHHFalta_': FaltaFactory
}


def load_from_csv_file(rows: list, table: str, logger: Logger) -> list[BaseCSVModel]:
    """
    Utility function to load data into model instances from CSV data.
    :param rows: CSV data without header
    :param table: DB Table name
    :param logger: Loger object
    :return: model_data_list
    """
    model = model_mapper[table].pydantic_model

    try:
        model_data_list = [model.from_csv_row(line) for line in rows]
        logger.info(f"{len(model_data_list)} objects from class '{model.__name__}' created from {len(rows)} CSV rows.")
    except ValidationError as e:
        logger.error(f"Error during CSV validation:\n{e}")
        raise ValueError("Error during CSV validation")

    return model_data_list
