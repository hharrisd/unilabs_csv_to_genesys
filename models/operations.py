from typing import Type

from sqlalchemy.orm import Session, DeclarativeBase

from models import BaseCSVModel, model_mapper


def insert_records(records: list[BaseCSVModel], session: Session, table: str):
    """
    Perform a insert operation of a list of models into a given table
    :param records: List of models to insert
    :param session: DB session object
    :param table: Table to perform the insertion
    :return:
    """
    EntityDB = model_mapper[table]['orm_model']

    for record in records:
        entity_db = EntityDB(**record.model_dump())
        session.add(entity_db)

    session.commit()
