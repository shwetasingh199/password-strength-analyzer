import secrets
import string


def generate_password(
    length: int = 20,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_numbers: bool = True,
    use_symbols: bool = True
) -> str:

    if length < 12:
        raise ValueError(
            "Password length must be at least 12."
        )

    character_pool = ""

    if use_uppercase:
        character_pool += string.ascii_uppercase

    if use_lowercase:
        character_pool += string.ascii_lowercase

    if use_numbers:
        character_pool += string.digits

    if use_symbols:
        character_pool += "!@#$%^&*()-_=+"

    if not character_pool:
        raise ValueError(
            "At least one character type must be selected."
        )

    password = "".join(
        secrets.choice(character_pool)
        for _ in range(length)
    )

    return password