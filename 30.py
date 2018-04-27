# encoding=utf-8
from datetime import datetime


# class Bucket(object):
# 	def __init__(self, peroid):
# 		self.peroid_delta = timedelta(seconds=peroid)
# 		self.reset_time = datetime.now()
# 		self.quota = 0
#
# 	def __repr__(self):
# 		return 'Bucket(quota=%d' % self.quota
#
#
# def fill(bucket, amount):
# 	now = datetime.now()
# 	if now - bucket.reset_time > bucket.peroid_delta:
# 		bucket.quota = 0
# 		bucket.reset_time = now
# 	bucket.quota += amount
#
#
# def deduct(bucket, amount):
# 	now = datetime.now()
# 	if now - bucket.reset_time > bucket.peroid_delta:
# 		return False
# 	if bucket.quota - amount < 0:
# 		return False
# 	bucket.quota -= amount
# 	return True
#
#
# bucket = Bucket(60)
# fill(bucket,100)
# print(bucket)
#
# if deduct(bucket,99):
# 	print('Had 99 quota')
# else:
# 	print('Not enough for 99 quota')
#
#
# print(bucket)
#

class Bucket(object):
	def __init__(self,period):
		self.period_delta = timedelta(seconds=period)
		self.reset_time = datetime.now()
		self.max_quota = 0
		self.quota_consumed = 0

	def __repr__(self):
		return ('Bucket(max_quota=%d),quota_comsumed=%d'%(self.max_quota,self.quota_consumed))

	@property
	def quota(self):
		return('Bucket(max_quota=%d,quota_comsume=%d)'%(self.max_quota,self.quota_consumed))

	@quota.setter
	def quota(self,amount):
		delta = self.max_quota = amount
		if amount==0:
			self.quota_consumed = 0
			self.max_quota = 0
		elif delta<0:
			assert self.quota_consumed ==0
			self.max_quota = amount
		else:
			assert self.max_quota >= self.quota_consumed
			self.quota_consumed+=delta

bucket = Bucket(60)
print('Initial',bucket)
