def validate_ingredient_name(raw_ingredient_name: str) -> tuple[bool, str]:
    if raw_ingredient_name.strip() >= 200:
        return False, 'Name is too long'
    else:
        return True, 'Ingredient name is valid'
