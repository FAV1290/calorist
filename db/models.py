import uuid
import datetime
import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column


from db import Base


class Ingredient(Base):
    __tablename__ = 'ingredients'
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    name: Mapped[str] = mapped_column(sqlalchemy.String(256), nullable=False)
    owner_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=True)
    kcal: Mapped[float] = mapped_column(sqlalchemy.Float, nullable=True)
    proteins: Mapped[float] = mapped_column(sqlalchemy.Float, nullable=True)
    fats: Mapped[float] = mapped_column(sqlalchemy.Float, nullable=True)
    carbohydrates: Mapped[float] = mapped_column(sqlalchemy.Float, nullable=True)
    creator_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)


class Dish(Base):
    __tablename__ = 'dishes'
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    name: Mapped[str] = mapped_column(sqlalchemy.String(256), nullable=False)
    owner_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=True)


class DishComponent(Base):
    __tablename__ = 'dish_components'
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    dish_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=False)
    ingredient_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=False)
    weight_grams: Mapped[float] = mapped_column(sqlalchemy.Float, nullable=False)


class Userprofile(Base):
    __tablename__ = 'user_profiles'
    user_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(sqlalchemy.types.BigInteger)
    name: Mapped[str] = mapped_column(sqlalchemy.String(128), nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(bind=Base.engine)