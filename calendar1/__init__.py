from datetime import datetime


def is_weekday():
    """This function checks if today is a weekday (Monday to Friday)
    and returns True if it is, and False if it is not."""
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5
