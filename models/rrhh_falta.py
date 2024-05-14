import datetime
from datetime import date, datetime

from sqlalchemy import Column, String, DateTime, Integer, Numeric, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Tmp_RRHHFalta(Base):
    __tablename__ = 'TMP_RRHHFalta'

    Op: Mapped[int] = mapped_column(Numeric(18, 0), primary_key=True, autoincrement=True)
    ID_Personal: Mapped[str] = mapped_column(String(20), nullable=False)
    Fecha: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    ID_TipoFalta: Mapped[int] = mapped_column(Integer, nullable=False)
    Descripcion: Mapped[str] = mapped_column(String(250), nullable=True)
    Estado: Mapped[int] = mapped_column(Integer, nullable=False)
    Condicion: Mapped[int] = mapped_column(Integer, nullable=False)
    Cantidad_Horas: Mapped[float] = mapped_column(Float, nullable=False)
    Observaciones: Mapped[str] = mapped_column(String(250), nullable=True)
    OpTransferido: Mapped[int] = mapped_column(Integer, nullable=True)
    OpTransferidoIntento: Mapped[int] = mapped_column(Numeric(18, 0), nullable=True)
    OpTransferidoFechaHora: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    OpTransferidoUsuario: Mapped[int] = mapped_column(Integer, nullable=True)

    def __repr__(self):
        return (
            f"TMP_RRHHFalta(ID_Personal='{self.ID_Personal}', Fecha='{self.Fecha}', ID_TipoFalta={self.ID_TipoFalta}, "
            f"Descripcion='{self.Descripcion}', Estado={self.Estado}, Condicion={self.Condicion}, "
            f"Cantidad_Horas={self.Cantidad_Horas}, Observaciones='{self.Observaciones}')"
        )
