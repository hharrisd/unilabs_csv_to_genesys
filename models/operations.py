from logging import Logger

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
    EntityDB = model_mapper[table].orm_model

    try:
        for record in records:
            entity_db = EntityDB(**record.model_dump())
            session.add(entity_db)

        session.commit()
        logger.info(f"{len(records)} inserted on table {EntityDB.__table__}")
    except SQLAlchemyError as e:
        logger.error(f"Error during insertion en entity {EntityDB.__name__}: {e}")
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
            result = session.execute(statement=statement, params=params)
            logger.info(f"Procedure {query} executed.")
            logger.debug(f"Procedure {query} result: {result.fetchall()}")
        except SQLAlchemyError as e:
            logger.error(f"Error calling {query=}; {params=}: {e}")
            raise OperationalException("Error during insert records")
