# encoding=utf-8

# stats = {}
# key = 'my_counter'
# if key not in stats:
# 	stats[key] = 0
# stats[key] += 1
#
#
# print(stats)
from collections import defaultdict
from heapq import heappush, heappop, nsmallest

stats = defaultdict(int)

print(stats)

stats['my_counter'] += 1

print(stats)

## 堆队列

a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)

print(a)

# print(heappop(a), heappop(a), heappop(a), heappop(a))

# assert a[0] == nsmallest(1, a)[0] == 3

print('before',a)
a.sort()
print('after',a)



