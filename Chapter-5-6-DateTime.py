"""
Chapter 5: Date and Time
Section 5.1: Parsing a string into a timezone aware datetime object
Python 3.2+ has support for %z format when parsing a string into a datetime object.
    UTC offset in the form +HHMM or -HHMM (empty string if the object is naive).

Python 3.x Version ≥ 3.2
import datetime
dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")

For other versions of Python, you can use an external library such as dateutil, which makes parsing a string with
timezone into a datetime object is quick.
import dateutil.parser
dt = dateutil.parser.parse("2016-04-15T08:27:18-0500")
The dt variable is now a datetime object with the following value:
datetime.datetime(2016, 4, 15, 8, 27, 18, tzinfo=tzoffset(None, -18000))


Section 5.2: Constructing timezone-aware datetimes
By default all datetime objects are naive. To make them timezone-aware, you must attach a tzinfo object, which
provides the UTC offset and timezone abbreviation as a function of date and time.

Fixed Offset Time Zones:

#Python 3.x Version < 3.2
from datetime import datetime, timedelta
from dateutil import tz
JST = tz.tzoffset('JST', 9 * 3600) # 3600 seconds per hour
dt = datetime(2015, 1, 1, 12, 0, tzinfo=JST)
print(dt)
# 2015-01-01 12:00:00+09:00
print(dt.tzname)
# 'JST'

Zones with daylight savings time:
python standard libraries do not provide a standard class, so it is necessary to
use a third party library. pytz and dateutil are popular libraries providing time zone classes.

Section 5.3: Computing time dierences
the timedelta module comes in handy to compute differences between times:

Section 5.4: Basic datetime objects usage
The datetime module contains three primary types of objects - date, time, and datetime.

Section 5.5: Switching between time zones
To switch between time zones, you need datetime objects that are timezone-aware.
utc = tz.tzutc()
local = tz.tzlocal()
utc_now = datetime.utcnow()
utc_now # Not timezone-aware.
utc_now = utc_now.replace(tzinfo=utc)
utc_now # Timezone-aware.
local_now = utc_now.astimezone(local)
local_now # Converted to local time.

Section 5.6: Simple date arithmetic
Dates don't exist in isolation. It is common that you will need to find the amount of time between dates or
determine what the date will be tomorrow. This can be accomplished using timedelta objects

Section 5.7: Converting timestamp to datetime
The datetime module can convert a POSIX timestamp to a ITC datetime object.

Section 5.8: Subtracting months from a date accurately
Using the calendar module


Section 5.9: Parsing an arbitrary ISO 8601 timestamp with minimal libraries
There is a single-file library called iso8601 which properly parses ISO 8601 timestamps and only them.
It supports fractions and timezones, and the T separator all with a single function:

Section 5.10: Get an ISO 8601 timestamp

Section 5.11: Parsing a string with a short time zone name into
GoalKicker.com – Python® Notes for Professionals 47
a timezone aware datetime object

Section 5.12: Fuzzy datetime parsing (extracting datetime out of a text)

Section 5.13: Iterate over dates


Chapter 6: Date Formatting

Section 6.1: Time between two date-times
from datetime import datetime
a = datetime(2016,10,06,0,0,0)
b = datetime(2016,10,01,23,59,59)
a-b
# datetime.timedelta(4, 1)
(a-b).days
# 4
(a-b).total_seconds()
# 518399.0

Section 6.2: Outputting datetime object to string

Uses C standard format codes.
from datetime import datetime
datetime_for_string = datetime(2016,10,1,0,0)
datetime_string_format = '%b %d %Y, %H:%M:%S'
datetime.strftime(datetime_for_string,datetime_string_format)
# Oct 01 2016, 00:00:00


Section 6.3: Parsing string to datetime object
from datetime import datetime
datetime_string = 'Oct 1 2016, 00:00:00'
datetime_string_format = '%b %d %Y, %H:%M:%S'
datetime.strptime(datetime_string, datetime_string_format)
# datetime.datetime(2016, 10, 1, 0, 0)

"""
#Python 3.x Version ≥ 3.2
from datetime import datetime, timedelta, timezone
dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=9), 'JST'))
print(dt.tzname)


