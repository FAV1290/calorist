import uuid
import typing
import datetime
import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column


from db import Base


class Ingredient(Base):
    __tablename__ = 'ingredients'
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    name: Mapped[str] = mapped_column(sqlalchemy.String(256), nullable=False)
    owner_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=True)
    kcals: Mapped[float] = mapped_column(sqlalchemy.Float, nullable=True)
    proteins: Mapped[float] = mapped_column(sqlalchemy.Float, nullable=True)
    fats: Mapped[float] = mapped_column(sqlalchemy.Float, nullable=True)
    carbohydrates: Mapped[float] = mapped_column(sqlalchemy.Float, nullable=True)
    creator_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)

    @classmethod
    def fetch_user_ingredients(cls, user_id: uuid.UUID) -> list[typing.Self]:
        return cls.query.filter(cls.owner_id == user_id).order_by(cls.name).all()


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


class UserProfile(Base):
    __tablename__ = 'user_profiles'
    user_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(sqlalchemy.types.BigInteger, unique=True)
    name: Mapped[str] = mapped_column(sqlalchemy.String(128), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)

    @classmethod
    def find_profile_id_by_telegram_id(cls, target_telegram_id: int) -> uuid.UUID | None:
        target_profile = cls.query.filter(cls.telegram_id == target_telegram_id).first()
        return target_profile.user_id if target_profile else None


if __name__ == '__main__':
    Base.metadata.create_all(bind=Base.engine)
