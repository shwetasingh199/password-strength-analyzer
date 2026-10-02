def calculate_score(
    length_metrics: dict,
    character_metrics: dict,
    findings: list,
    is_common: bool
) -> int:

    score = 0

    # -------------------------
    # Length: maximum 35
    # -------------------------

    score += length_metrics["score"]

    # -------------------------
    # Character diversity: max 15
    # -------------------------

    character_types = character_metrics["character_type_count"]

    diversity_score = min(
        character_types * 3,
        15
    )

    score += diversity_score

    # -------------------------
    # Unique character ratio: max 10
    # -------------------------

    ratio = character_metrics["unique_character_ratio"]

    unique_score = round(ratio * 10)

    score += min(unique_score, 10)

    # -------------------------
    # Additional unpredictability
    # -------------------------

    if length_metrics["length"] >= 16:
        score += 10

    # -------------------------
    # Common password penalty
    # -------------------------

    if is_common:
        score -= 35

    # -------------------------
    # Pattern penalties
    # -------------------------

    for finding in findings:

        finding_lower = finding.lower()

        if "keyboard" in finding_lower:
            score -= 15

        elif "sequence" in finding_lower:
            score -= 10

        elif "repeated" in finding_lower:
            score -= 10

        elif "predictable" in finding_lower:
            score -= 10

        elif "year" in finding_lower:
            score -= 10

    return max(0, min(score, 100))


def classify_score(score: int) -> str:

    if score <= 20:
        return "VERY WEAK"

    if score <= 40:
        return "WEAK"

    if score <= 60:
        return "MODERATE"

    if score <= 80:
        return "STRONG"

    return "VERY STRONG"