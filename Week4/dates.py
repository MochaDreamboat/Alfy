import datetime
import pytz

# Naive dates/times: Can't account for Timezones or DST
# Aware dates/times CAN

# Normal date (year, month, date)
# Use regular integers with no leading zero (otherwise results in syntax error)
d = datetime.date(2022, 7, 24)

# Grab today's date:
# Max args: yr, month, date, hr, min, sec, microsecond
tday = datetime.date.today()

# Just grab year
print(tday.year)

# Just grab day
print(tday.day)

# Weekday by integer (Monday starts at 0)
print(tday.weekday()) # i.e. Wednesday returns 2

#Weekday by integer (Monday starts at 1)
print(tday.isoweekday) # i.e. Wednesday returns 3


# Time delta (diff between two dates/times)
tdelta = datetime.timedelta(days=7)

# Calcuating w/ tdelta
print(tday + tdelta) # Returns date 7 days in the future
print(tday - tdelta) # Returns date 7 days ago

# Evaluating a tdelta
bday = datetime.date(2023, 9, 24)

till_bday = bday - tday
print(till_bday) # x days, 00:00:00
print(till_bday.days) # 60
print(till_bday.total_seconds()) # x seconds to the nearest tenth of second

# Create local time (naive)
# Args: Hrs, min, sec, microsec
t = datetime.time(9, 30, 45, 100000)

# Max args: yr, month, date, hr, min, sec, microsecond
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)

# All inclusive
print(dt.time())
print(dt.year()) ###

                            # Can be different time units too
tdelta = datetime.timedelta(days=7)
print(dt + tdelta)


# Current local date/time w/ timezone of None
dt_today = datetime.datetime.today()

# Gives option to pass timezone (as optional arg)
dt_now = datetime.datetime.now()

# Timezone-aware timezone using utc/pytz
dt_test = datetime.datetime(2022, 11, 23, 1, 31, 00, tzinfo=pytz.UTC)
print(dt_test)

dt_now2 = datetime.datetime.now(tz=pytz.UTC)
print(dt_now2)

dt_cst = dt_now2.astimezone(pytz.timezone('US/Central'))
print(dt_cst)

# Making naive time timezone aware

# 1. Declare naive time
dt_naive = datetime.datetime.now()

# 2. Declare timezone from pytz
cst_tz = pytz.timezone('US/Central')

# 3. Run localize method on timezone and pass naive time as arg.
# Naive time is now aware!

dt_central = cst_tz.localize(dt_naive)

# Given the aware time, you can now convert it into different timezones
# in new variables.
# Running .astimezone() method while time is naive will throw error
dt_east = dt_central.astimezone(pytz.timezone('US/Eastern'))
print(dt_central)