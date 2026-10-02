def analyze_length(password: str) -> dict:
    """
    Analyze password length.

    The length score is educational and does not determine
    password security by itself.
    """

    length = len(password)

    if length < 8:
        category = "VERY SHORT"
        contribution = 5
    elif length <= 11:
        category = "SHORT"
        contribution = 15
    elif length <= 15:
        category = "BETTER LENGTH"
        contribution = 25
    else:
        category = "STRONG LENGTH"
        contribution = 35

    return {
        "length": length,
        "category": category,
        "score": contribution
    }