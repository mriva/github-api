import pytz
from datetime import datetime


def localized_timestamp(datetime_string):
    local_tz = pytz.timezone('Europe/Rome')

    utc_timestamp = datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%S%z')
    return utc_timestamp.astimezone(local_tz)


def timestamp_diff(start, end):
    start_ts = datetime.strptime(start, '%Y-%m-%dT%H:%M:%S%z')
    end_ts = datetime.strptime(end, '%Y-%m-%dT%H:%M:%S%z')

    return (end_ts - start_ts)
