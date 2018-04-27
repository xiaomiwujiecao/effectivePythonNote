from queue import Queue
from threading import Thread

import time

# queue = Queue(1)
#
# def consumer():
#
# 	print('Consumer waiting')
# 	time.sleep(0.1)
# 	queue.get()
# 	print('comsumer got 1')
# 	queue.get()
# 	print('comsumer got 2')
# 	print('Consumer done')
#
# thread = Thread(target=consumer)
#
# thread.start()
#
# print('producer putting')
#
# queue.put(object())
# queue.put(object())
#
# thread.join()
#
# print('producer done')

in_queue = Queue()

def consumer():
	print("consumer waiting")
	work = in_queue.get()
	print('consumer working')

	print('comsumer done')

	in_queue.task_done()

Thread(target=consumer).start()

in_queue.put(object())
print('producer waiting')
in_queue.join()
print('producer done')

class ClosableQueue(Queue):
	SENTINEL = object()

	def close(self):
		self.put(self.SENTINEL)

	def __iter__(self):
		while True:
			item = self.get()
			try:
				if item  is self.SENTINEL:
					return
				yield item
			finally:
				self.task_done()


class StopableWorker(Thread):
	def __init__(self,func,in_queue,out_queque):
		pass

	def run(self):
		for item in self.in_queue:
			result = self.func(item)
			self.out_queque.put(result)

downlaod_queue = ClosableQueue()

threads = []