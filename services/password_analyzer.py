from .length_analyzer import analyze_length
from .character_analyzer import analyze_characters
from .common_password_checker import is_common_password
from .pattern_detector import (
    detect_sequences,
    detect_keyboard_patterns,
    detect_repetition,
    detect_predictable_structure
)
from .entropy_estimator import estimate_theoretical_entropy
from .scoring_engine import (
    calculate_score,
    classify_score
)
from .suggestion_engine import generate_suggestions
from .policy_checker import check_policy


def analyze_password(
    password: str,
    context: dict | None = None
) -> dict:

    context = context or {}

    # -------------------------
    # Basic metrics
    # -------------------------

    length_metrics = analyze_length(password)

    character_metrics = analyze_characters(password)

    # -------------------------
    # Common password
    # -------------------------

    common = is_common_password(password)

    # -------------------------
    # Pattern detection
    # -------------------------

    findings = []

    findings.extend(
        detect_sequences(password)
    )

    findings.extend(
        detect_keyboard_patterns(password)
    )

    findings.extend(
        detect_repetition(password)
    )

    findings.extend(
        detect_predictable_structure(password)
    )

    # -------------------------
    # Personal context
    # -------------------------

    personal_info_found = False

    for value in context.values():

        if not value:
            continue

        value = str(value).strip().lower()

        if len(value) >= 3 and value in password.lower():
            personal_info_found = True
            findings.append(
                "Password appears to contain personal information."
            )
            break

    # -------------------------
    # Common password finding
    # -------------------------

    if common:
        findings.append(
            "Password matches a commonly used password."
        )

    findings = list(dict.fromkeys(findings))

    # -------------------------
    # Entropy estimate
    # -------------------------

    entropy = estimate_theoretical_entropy(
        password,
        character_metrics
    )

    # -------------------------
    # Score
    # -------------------------

    score = calculate_score(
        length_metrics,
        character_metrics,
        findings,
        common
    )

    classification = classify_score(score)

    # -------------------------
    # Suggestions
    # -------------------------

    suggestions = generate_suggestions(
        findings,
        length_metrics,
        common,
        personal_info_found
    )

    # -------------------------
    # Policy
    # -------------------------

    policy = check_policy(
        password,
        common,
        personal_info_found
    )

    # -------------------------
    # Safe response
    # -------------------------

    return {
        "score": score,
        "classification": classification,

        "findings": findings,

        "suggestions": suggestions,

        "metrics": {
            "length": length_metrics["length"],
            "length_category": length_metrics["category"],
            "uppercase": character_metrics["has_uppercase"],
            "lowercase": character_metrics["has_lowercase"],
            "digits": character_metrics["has_digit"],
            "symbols": character_metrics["has_symbol"],
            "spaces": character_metrics["has_space"],
            "unique_character_count":
                character_metrics["unique_character_count"],
            "character_type_count":
                character_metrics["character_type_count"],
            "unique_character_ratio":
                character_metrics["unique_character_ratio"],
            "theoretical_entropy_bits": entropy,
            "common_password": common,
            "personal_information_detected":
                personal_info_found,
            "pattern_count": len(findings)
        },

        "policy": policy
    }