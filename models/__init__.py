from logging import Logger
from typing import Type

from pydantic import ValidationError

from .autorizar_h_e import AutorizarHE, AutorizarHEFactory
from .base_models import BaseCSVModel, BaseModelFactory
from .concepto_aplicado import ConceptoAplicado, ConceptoAplicadoFactory
from .dato_extra import DatoExtra, DatoExtraFactory
from .falta import Falta, FaltaFactory
from .licencia import Licencia, LicenciaFactory
from .persona_natural import PersonaNatural, PersonaNaturalFactory
from .personal import Personal, PersonalFactory
from .vacacion import Vacacion, VacacionFactory

model_mapper: dict[str, Type[BaseModelFactory]] = {
    '_TMP_RRHHAutorizarHE_': AutorizarHEFactory,
    '_TMP_RRHHConceptoAplicado_': ConceptoAplicadoFactory,
    '_TMP_RRHHDatoExtra_': DatoExtraFactory,
    '_TMP_RRHHFalta_': FaltaFactory,
    '_TMP_RRHHLicencia_': LicenciaFactory,
    '_TMP_PersonaNatural_': PersonaNaturalFactory,
    '_TMP_RRHHPersonal_': PersonalFactory,
    '_TMP_RRHHVacacion_': VacacionFactory,
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
        logger.error(f"Error durante la validación del archivo CSV:\n{e}")
        raise ValueError(f"Error durante la validación del archivo CSV:\n{e}")

    return model_data_list
