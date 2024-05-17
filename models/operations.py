from logging import Logger

import pyodbc
from sqlalchemy import sql
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from models import BaseCSVModel, model_mapper


class OperationalException(Exception):
    pass


def insert_records(records: list[BaseCSVModel], session: Session, table: str, logger: Logger) -> None:
    """
    Perform a insert operation of a list of models into a given table
    :param records: List of models to insert
    :param session: DB session object
    :param table: Table to perform the insertion
    :param logger: Logger object
    """
    orm_entity_class = model_mapper[table].orm_model

    logger.debug(f"About to insert {len(records)} records on class {orm_entity_class.__name__}")

    try:
        for record in records:
            entity_object = orm_entity_class(**record.model_dump())
            session.add(entity_object)

        session.commit()
        logger.info(f"{len(records)} inserted on table {orm_entity_class.__table__}")
    except (SQLAlchemyError, pyodbc.Error) as e:
        logger.error(f"Error during insertion on entity {orm_entity_class.__name__}: \n{e}")
        raise OperationalException("Error during insert records")


def execute_procedures(session: Session, table: str, logger: Logger) -> None:
    """
    Execute stored procedures
    :param session: DB session object
    :param table: Table to get the related stored procedures
    :param logger: Logger object
    """
    for procedure in model_mapper[table].procedures:
        query = params = None
        try:
            query, params = procedure
            statement = sql.text(query)
            session.execute(statement=statement, params=params)
            logger.info(f"Procedure {query} executed.")
        except SQLAlchemyError as e:
            logger.error(f"Error calling {query=}; {params=}: {e}")
            raise OperationalException("Error during insert records")
