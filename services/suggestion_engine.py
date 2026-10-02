def generate_suggestions(
    findings: list,
    length_metrics: dict,
    is_common: bool,
    personal_info_found: bool
) -> list:

    suggestions = []

    if length_metrics["length"] < 12:
        suggestions.append(
            "Consider using a longer password or passphrase."
        )

    if is_common:
        suggestions.append(
            "Avoid commonly used passwords."
        )

    for finding in findings:

        text = finding.lower()

        if "sequence" in text:
            suggestions.append(
                "Remove predictable numeric or alphabetic sequences."
            )

        if "keyboard" in text:
            suggestions.append(
                "Avoid predictable keyboard sequences such as qwerty."
            )

        if "repeated" in text:
            suggestions.append(
                "Avoid repeated characters or repeated substrings."
            )

        if "predictable" in text:
            suggestions.append(
                "Avoid predictable word + number combinations."
            )

        if "year" in text:
            suggestions.append(
                "Avoid using predictable years or dates."
            )

    if personal_info_found:
        suggestions.append(
            "Avoid including your name, birth year, company, or college."
        )

    suggestions.extend([
        "Avoid reusing passwords across different accounts.",
        "Consider using a password manager.",
        "Enable MFA where available."
    ])

    # Remove duplicates while preserving order
    return list(dict.fromkeys(suggestions))