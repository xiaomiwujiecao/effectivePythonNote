# encoding=utf-8

import select
from threading import Thread
from time import time


def slow_system_call():
	select.select([],[],[],0.1)

start = time()
threads = []

for _ in range(5):
	thread = Thread(target=slow_system_call)
	thread.start()
	threads.append(thread)

end  = time()

def compute_helicopter_location():
	pass

for i in range(5):
	compute_helicopter_location(i)

for thread in threads:
	thread.join()


print('Took %.3f seconds' %(end-start))
