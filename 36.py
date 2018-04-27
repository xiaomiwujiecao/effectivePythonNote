# encoding=utf-8
import subprocess

# proc = subprocess.Popen(
#
# 	['echo','Hello from the child'],
# 	stdout=subprocess.PIPE
# )
#
# out,err = proc.communicate()
#
# print(out.decode('utf-8'))

# proc = subprocess.Popen(
# 	['sleep','0.3']
# )
#
# while proc.poll() is None:
# 	print('working')
#
#
# print('Exit status',proc.poll())
from time import time

import os


def run_sleep(period):

	proc = subprocess.Popen(
		['sleep',str(period)]
	)
	return proc

start = time()

procs =[]

for _ in range(10):
	proc = run_sleep(0.1)
	procs.append(proc)


for proc in procs:
	proc.communicate()


end = time()

print(end)

print('finished in %.3f seconds' %(end - start))


def run_openssl(data):
	env = os.environ.copy()
	env['password'] = b'\xe24U\n\xd0Q13S\x11'
	proc = subprocess.Popen(
		['openssl','enc','-des3','-pass','env:password'],
		env=env,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE
	)

	proc.stdin.write(data)
	proc.stdin.flush()
	return proc

procs =[]

for _ in range(3):
	data = os.urandom(10)
	proc = run_openssl(data)
	procs.append(proc)

for proc in procs:
	out,err = proc.communicate()
	print(out[-10:])

def run_md5(input_stdin):
	proc = subprocess.Popen(
		['md5'],
		stdin=input_stdin,
		stdout=subprocess.PIPE
	)


input_procs = []
hash_procs = []

for _ in range(3):
	data = os.urandom(10)
	proc = run_openssl(data)
	input_procs.append(proc)
	hash_proc =run_md5(proc.stdout)
	hash_procs.append(hash_proc)


for proc in input_procs:
	proc.communicate()

for proc in hash_procs:
	out,err = proc.communicate()
	print(out.strip())

proc = run_sleep(10)

try:
	proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
	proc.terminate()
	proc.wait()

print('Exit status',proc.poll())


