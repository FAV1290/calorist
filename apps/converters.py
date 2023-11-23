import uuid
import datetime


from db.models import Ingredient, UserProfile


def compose_ingredient_from(
    name: str,
    owner_id: uuid.UUID,
    kcals: float,
    proteins: float,
    fats: float,
    carbohydrates: float
) -> Ingredient:
    return Ingredient(
        id=uuid.uuid4(),
        name=name,
        owner_id=owner_id,
        kcals=kcals,
        proteins=proteins,
        fats=fats,
        carbohydrates=carbohydrates,
        creator_id=owner_id,
        created_at=datetime.datetime.now()
    )


def compose_profile_from(telegram_id: int, name: str) -> UserProfile:
    return UserProfile(
        user_id=uuid.uuid4(),
        telegram_id=telegram_id,
        name=name,
        created_at=datetime.datetime.now(),
    )
