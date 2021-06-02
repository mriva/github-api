import pytz
from datetime import datetime


def localized_timestamp(datetime_string):
    local_tz = pytz.timezone('Europe/Rome')

    utc_timestamp = datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%S%z')
    return utc_timestamp.astimezone(local_tz)
