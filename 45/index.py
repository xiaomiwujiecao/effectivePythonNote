# encoding=utf-8

from time import localtime,strftime,mktime,strptime

now = 1407694710
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format,local_tuple)
print(time_str)

time_tuple2 = strptime(time_str,time_format)
utc_now = mktime(time_tuple2)
print(utc_now)

parse_format = '%Y-%m-%d %H:%M:%S %Z'
depart_sfo = '2014-05-02 15:46:16 PDT'
time_tuple3 = strptime(depart_sfo,parse_format)
time_str2 = strftime(time_format,time_tuple3)

print(time_str)