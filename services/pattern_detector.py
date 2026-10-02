import re


KEYBOARD_PATTERNS = [
    "qwerty",
    "asdf",
    "zxcv",
    "qwertyuiop",
    "asdfgh",
    "zxcvbn",
]


def detect_sequences(password: str) -> list[str]:
    """Detect ascending and descending alphanumeric sequences."""

    findings = []

    if len(password) < 3:
        return findings

    for i in range(len(password) - 2):
        chunk = password[i:i + 3]

        values = [ord(char.lower()) for char in chunk]

        if values[1] == values[0] + 1 and values[2] == values[1] + 1:
            findings.append(
                f"Ascending sequence detected: {chunk}"
            )

        elif values[1] == values[0] - 1 and values[2] == values[1] - 1:
            findings.append(
                f"Descending sequence detected: {chunk}"
            )

    return list(dict.fromkeys(findings))


def detect_keyboard_patterns(password: str) -> list[str]:
    """Detect simple keyboard-style patterns."""

    password_lower = password.lower()

    findings = []

    for pattern in KEYBOARD_PATTERNS:
        if pattern in password_lower:
            findings.append(
                f"Keyboard pattern detected: {pattern}"
            )

    return findings


def detect_repetition(password: str) -> list[str]:
    """Detect repeated characters and repeated substrings."""

    findings = []

    # Repeated same character, e.g. aaaa
    if re.search(r"(.)\1{2,}", password):
        findings.append(
            "Repeated character pattern detected."
        )

    # Repeated substring, e.g. abcabc
    for size in range(2, max(2, len(password) // 2 + 1)):

        if len(password) < size * 2:
            continue

        pattern = password[:size]

        if pattern * 2 in password:
            findings.append(
                "Repeated substring pattern detected."
            )
            break

    return findings


def detect_predictable_structure(password: str) -> list[str]:
    """Detect common word + number/year style structures."""

    findings = []

    lowered = password.lower()

    common_words = [
        "password",
        "welcome",
        "admin",
        "hello",
        "letmein",
        "qwerty"
    ]

    for word in common_words:

        if lowered.startswith(word):

            remaining = lowered[len(word):]

            if remaining.isdigit():
                findings.append(
                    "Predictable word + number structure detected."
                )

                if len(remaining) == 4:
                    findings.append(
                        "Possible year/date-like suffix detected."
                    )

    return findings