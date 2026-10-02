from pathlib import Path


COMMON_PASSWORD_FILE = (
    Path(__file__).resolve()
    .parents[2]
    / "data"
    / "common_passwords.txt"
)


def load_common_passwords() -> set[str]:
    """Load educational common-password list."""

    if not COMMON_PASSWORD_FILE.exists():
        return set()

    with open(
        COMMON_PASSWORD_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return {
            line.strip().lower()
            for line in file
            if line.strip()
        }


def is_common_password(password: str) -> bool:
    """Return True if password matches the local demo list."""

    common_passwords = load_common_passwords()

    return password.lower() in common_passwords