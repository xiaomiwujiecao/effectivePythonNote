# encoding=utf-8
from threading import Lock

lock = Lock()

with lock:
	print('lock is held')

lock.acquire()
try:
	print('lock is held')
finally:
	lock.release()


