from datetime import datetime, timezone


def get_age_from_dob(now: datetime, dob: datetime) -> int:
    return int((now - dob).days / 365)
