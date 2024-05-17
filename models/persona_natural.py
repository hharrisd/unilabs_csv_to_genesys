from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from models.base_models import BaseCSVModel, BaseORM, BaseModelFactory


class PersonaNatural(BaseCSVModel):
    Nombre1: str
    Nombre2: Optional[str] = None
    ApellidoPaterno: str
    ApellidoMaterno: Optional[str] = None
    DNI: str
    RUC: Optional[str] = None


class PersonaNaturalEntity(BaseORM):
    __tablename__ = 'TMP_PersonaNatural'

    Op: Mapped[int] = mapped_column(Numeric(18, 0), primary_key=True, autoincrement=True)
    Nombre1: Mapped[str] = mapped_column(String(50), nullable=False)
    Nombre2: Mapped[str] = mapped_column(String(50), nullable=True)
    ApellidoPaterno: Mapped[str] = mapped_column(String(50), nullable=False)
    ApellidoMaterno: Mapped[str] = mapped_column(String(50), nullable=False)
    DNI: Mapped[str] = mapped_column(String(8), nullable=False)
    RUC: Mapped[str] = mapped_column(String(11), nullable=True)

    def __repr__(self):
        return (
            f"TMP_PersonaNatural(Nombre1='{self.Nombre1}', Nombre2='{self.Nombre2}', "
            f"ApellidoPaterno='{self.ApellidoPaterno}', ApellidoMaterno='{self.ApellidoMaterno}', "
            f"DNI='{self.DNI}', RUC='{self.RUC}')"
        )


@dataclass
class PersonaNaturalFactory(BaseModelFactory):
    pydantic_model = PersonaNatural
    orm_model = PersonaNaturalEntity
    procedures = [('EXEC sp_TMPPersonaNatural', None)]
