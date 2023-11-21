import uuid
import datetime


from db.models import Ingredient


def compose_ingredient_from(
    name: str,
    user_id: uuid.UUID,
    kcals: float,
    proteins: float,
    fats: float,
    carbohydrates: float
) -> Ingredient:
    return Ingredient(
        id=uuid.uuid4(),
        name=name,
        owner_id=user_id,
        kcals=kcals,
        proteins=proteins,
        fats=fats,
        carbohydrates=carbohydrates,
        creator_id=user_id,
        created_at=datetime.datetime.now()
    )