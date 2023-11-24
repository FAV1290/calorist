def validate_ingredient_name(
    raw_ingredient_name: str,
    user_ingredients_names: list[str],
) -> tuple[bool, str]:
    if len(raw_ingredient_name.strip()) >= 200:
        return False, 'Name is too long'
    elif raw_ingredient_name.lower() in user_ingredients_names:
        return False, 'Ingredient with this name already exists'
    else:
        return True, 'Ingredient name is valid'


def validate_nutrition_facts(raw_nutrition_facts: list[str]) -> tuple[bool, str]:
    if len(raw_nutrition_facts) != 4:
        return False, 'Incorrect arguments quantity'
    elif not all(map(lambda x: x.replace('.', '').isdigit(), raw_nutrition_facts)):
        return False, 'Incorrect argument(s) value(s)'
    else:
        return True, 'Nutrition facts are valid'
