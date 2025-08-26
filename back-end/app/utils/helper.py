from datetime import datetime, timezone


def get_age_from_dob(now: datetime, dob: datetime) -> int:
    """Get the age(years) as integer from a given dateOfBirth in datetime."""
    return int((now - dob).days / 365)
