import math


def estimate_theoretical_entropy(
    password: str,
    character_metrics: dict
) -> float:
    """
    Estimate theoretical entropy.

    Formula:

        entropy = length * log2(character_pool)

    This assumes random character selection and therefore
    must NOT be treated as an exact prediction of security.
    """

    length = len(password)

    if length == 0:
        return 0.0

    pool = 0

    if character_metrics["has_lowercase"]:
        pool += 26

    if character_metrics["has_uppercase"]:
        pool += 26

    if character_metrics["has_digit"]:
        pool += 10

    if character_metrics["has_symbol"]:
        pool += 32

    if character_metrics["has_space"]:
        pool += 1

    if pool == 0:
        return 0.0

    entropy = length * math.log2(pool)

    return round(entropy, 2)