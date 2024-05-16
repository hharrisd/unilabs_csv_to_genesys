from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from pydantic import field_validator
from sqlalchemy import String, DateTime, Integer, Numeric, Float
from sqlalchemy.orm import Mapped, mapped_column

from models.base_models import BaseCSVModel, BaseORM, BaseModelFactory


class ConceptoAplicado(BaseCSVModel):
    ID_Personal: str
    ID_TipoConcepto: int
    Vigencia: datetime
    ID_Moneda: int
    Monto: float
    Observaciones: Optional[str] = None

    @field_validator('Vigencia', mode='before')
    def validate_vigencia(cls, value):
        return super().validate_fecha(value)


class ConceptoAplicadoEntity(BaseORM):
    __tablename__ = 'TMP_RRHHConceptoAplicado'

    Op: Mapped[int] = mapped_column(Numeric(18, 0), primary_key=True, autoincrement=True)
    ID_Personal: Mapped[str] = mapped_column(String(20), nullable=False)
    ID_TipoConcepto: Mapped[int] = mapped_column(Integer, nullable=False)
    Vigencia: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    ID_Moneda: Mapped[int] = mapped_column(Numeric(18, 0), nullable=False)
    Monto: Mapped[float] = mapped_column(Float, nullable=False)
    Observaciones: Mapped[str] = mapped_column(String(50), nullable=True)
    OpTransferido: Mapped[int] = mapped_column(Integer, nullable=True, default=1)
    OpTransferidoIntento: Mapped[int] = mapped_column(Numeric(18, 0), nullable=True, default=1)
    OpTransferidoFechaHora: Mapped[datetime] = mapped_column(DateTime, nullable=True, default=datetime.now())
    OpTransferidoUsuario: Mapped[int] = mapped_column(Integer, nullable=True, default=1)

    def __repr__(self):
        return (
            f"TMP_RRHHConceptoAplicado(ID_Personal='{self.ID_Personal}', ID_TipoConcepto={self.ID_TipoConcepto}, "
            f"Vigencia='{self.Vigencia}', ID_Moneda={self.ID_Moneda}, Monto={self.Monto}, "
            f"Observaciones='{self.Observaciones}')"
        )


@dataclass
class ConceptoAplicadoFactory(BaseModelFactory):
    pydantic_model = ConceptoAplicado
    orm_model = ConceptoAplicadoEntity
    procedures = [('EXEC sp_TMPRRHHConceptoAplicado', None)]
