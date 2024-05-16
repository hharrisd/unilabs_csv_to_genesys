from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from pydantic import field_validator
from sqlalchemy import String, DateTime, Integer, Numeric, Float
from sqlalchemy.orm import Mapped, mapped_column

from models.base_models import BaseCSVModel, BaseORM, BaseModelFactory


class Falta(BaseCSVModel):
    ID_Personal: str
    Fecha: datetime
    ID_TipoFalta: int
    Descripcion: Optional[str] = None
    Estado: int
    Condicion: int
    Cantidad_Horas: int
    Observaciones: Optional[str] = None

    @field_validator('Fecha', mode='before')
    def validate_fecha(cls, value):
        return super().validate_fecha(value)


class FaltaEntity(BaseORM):
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
    OpTransferido: Mapped[int] = mapped_column(Integer, nullable=True, default=1)
    OpTransferidoIntento: Mapped[int] = mapped_column(Numeric(18, 0), nullable=True, default=1)
    OpTransferidoFechaHora: Mapped[datetime] = mapped_column(DateTime, nullable=True, default=datetime.now())
    OpTransferidoUsuario: Mapped[int] = mapped_column(Integer, nullable=True, default=1)

    def __repr__(self):
        return (
            f"TMP_RRHHFalta(ID_Personal='{self.ID_Personal}', Fecha='{self.Fecha}', ID_TipoFalta={self.ID_TipoFalta}, "
            f"Descripcion='{self.Descripcion}', Estado={self.Estado}, Condicion={self.Condicion}, "
            f"Cantidad_Horas={self.Cantidad_Horas}, Observaciones='{self.Observaciones}')"
        )


@dataclass
class FaltaFactory(BaseModelFactory):
    pydantic_model = Falta
    orm_model = FaltaEntity
    procedures = [('EXEC sp_TMPRRHHFalta', None), ('EXEC sp_HelloName :name', {'name': 'Loki'})]
