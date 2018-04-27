# encoding=utf-8
import bisect

x = list(range(10**6))
# i = x.index(991234)

i = bisect.bisect_left(x,991234)
