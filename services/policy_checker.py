def check_policy(
    password: str,
    is_common: bool,
    personal_info_found: bool = False,
    minimum_length: int = 12
) -> dict:

    failures = []

    if len(password) < minimum_length:
        failures.append(
            f"Minimum length is {minimum_length} characters."
        )

    if is_common:
        failures.append(
            "Password is in the local common-password list."
        )

    if personal_info_found:
        failures.append(
            "Password appears to contain personal information."
        )

    return {
        "passed": len(failures) == 0,
        "failures": failures
    }