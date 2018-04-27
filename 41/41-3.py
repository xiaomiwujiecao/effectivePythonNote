# encoding=utf-8
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from time import time
def gcd(pair):
	a,b = pair
	low = min(a,b)
	for i in range(low,0,-1):
		if a %i ==0 and b%i==0:
			return i
numbers =	[(1963309,2265973),(2030677,3814172),
            (1551645,229620),(2039045,2020802)]
start = time()
pool = ProcessPoolExecutor(max_workers=2)
results = list(pool.map(gcd,numbers))
end = time()
print('took %.3f seconds' %(end-start))

