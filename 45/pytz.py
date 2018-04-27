# encoding=utf-8
from _datetime import datetime

import pytz as pytz

#
# print(pytz)

pacific = pytz.timezone('US/pacfic')

sf_dt =pacific.normalize(utc_dt.astimezone(pacific))