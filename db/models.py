import uuid
import datetime
import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column


from db import Base


class Ingredient(Base):
    __tablename__ = 'ingredients'
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    owner_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID)
    kcal: Mapped[float] = mapped_column(sqlalchemy.Float)
    proteins: Mapped[float] = mapped_column(sqlalchemy.Float)
    fats: Mapped[float] = mapped_column(sqlalchemy.Float)
    carbohydrates: Mapped[float] = mapped_column(sqlalchemy.Float)
    creator_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)
