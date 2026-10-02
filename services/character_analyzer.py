def analyze_characters(password: str) -> dict:
    """Analyze character diversity."""

    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)

    has_symbol = any(
        not c.isalnum() and not c.isspace()
        for c in password
    )

    has_space = any(c.isspace() for c in password)

    unique_count = len(set(password))
    length = len(password)

    unique_ratio = (
        unique_count / length
        if length > 0
        else 0
    )

    character_type_count = sum([
        has_lowercase,
        has_uppercase,
        has_digit,
        has_symbol,
        has_space
    ])

    return {
        "has_lowercase": has_lowercase,
        "has_uppercase": has_uppercase,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "has_space": has_space,
        "unique_character_count": unique_count,
        "character_type_count": character_type_count,
        "unique_character_ratio": round(unique_ratio, 2)
    }