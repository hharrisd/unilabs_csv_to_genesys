from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

from pydantic import field_validator
from sqlalchemy import String, DateTime, Integer, Numeric, Float
from sqlalchemy.orm import Mapped, mapped_column

from .base_models import BaseCSVModel, BaseORM, BaseModelFactory


class Vacacion(BaseCSVModel):
    ID_Personal: str
    Fecha: datetime
    Cantidad_Horas: int
    PeriodoAño: int
    Observaciones: Optional[str] = None

    @field_validator('Fecha', mode='before')
    def validate_fecha(cls, value):
        return super().validate_fecha(value)


class VacacionEntity(BaseORM):
    __tablename__ = 'TMP_RRHHVacacion'

    Op: Mapped[int] = mapped_column(Numeric(18, 0), primary_key=True, autoincrement=True)
    ID_Personal: Mapped[str] = mapped_column(String(20), nullable=False)
    Fecha: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    Cantidad_Horas: Mapped[float] = mapped_column(Float, nullable=False)
    PeriodoAño: Mapped[int] = mapped_column(Integer, nullable=False)
    Observaciones: Mapped[str] = mapped_column(String(250), nullable=True)
    OpTransferido: Mapped[int] = mapped_column(Integer, nullable=True, default=1)
    OpTransferidoIntento: Mapped[int] = mapped_column(Numeric(18, 0), nullable=True, default=1)
    OpTransferidoFechaHora: Mapped[datetime] = mapped_column(DateTime, nullable=True, default=datetime.now())
    OpTransferidoUsuario: Mapped[int] = mapped_column(Integer, nullable=True, default=1)

    def __repr__(self):
        return (
            f"TMP_RRHHVacacion(ID_Personal='{self.ID_Personal}', Fecha='{self.Fecha}', "
            f"Cantidad_Horas={self.Cantidad_Horas}, PeriodoAño={self.PeriodoAño}, "
            f"Observaciones='{self.Observaciones}')"
        )


@dataclass
class VacacionFactory(BaseModelFactory):
    pydantic_model = Vacacion
    orm_model = VacacionEntity
    procedures = [('EXEC sp_TMPRRHHVacacion', None)]
