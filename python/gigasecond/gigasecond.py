from datetime import datetime
import calendar
import time

def add_gigasecond(birth_date):
    """Add 1e9 seconds to supplied time"""
    s = time.mktime(birth_date.utctimetuple())
    s += 1e9
    return datetime.utcfromtimestamp(s)
