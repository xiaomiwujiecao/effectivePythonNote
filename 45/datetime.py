# encoding=utf-8

from _datetime import datetime,timezone
from time import mktime

time_format = '%Y-%m-%d %H:%M:%S'
now = datetime(2014,8,10,18,18,30)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(now_local)

time_str = '2014-08-10 11:18:30'
now = datetime.strptime(time_str,time_format)
time_tuple = now.timetuple()
utc_now = mktime(time_tuple)
print(utc_now)



