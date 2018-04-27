# encoding=utf-8
class OldRegistor(object):
	def __init__(self,ohms):
		self.ohms = ohms

	def get_ohms(self):
		return self.ohms

	def set_ohms(self,ohms):
		self.ohms = ohms

r0 = OldRegistor(50e3)
print('before:%5r '% r0.get_ohms())
r0.set_ohms(10e3)
print('after:%5r ' % r0.get_ohms())

class Register(object):
	def __init__(self,ohms):
		self.ohms = ohms
		self.voltage = 0
		self.current = 0

r1 = Register(50e3)
r1.ohms = 10e3

r1.ohms+=10e3

class VoltageRegistance(Register):
	def __init__(self,ohms):
		super().__init__(ohms)
		self._votage = 0

	@property
	def voltage(self):
		return self.voltage

	@voltage.setter
	def voltage(self,voltage):
		self._votage = voltage
		self.current = self._votage/self.ohms

r2 = VoltageRegistance(1e3)

print('before: %5r amps' % r2.current)
r2.voltage = 10
print('after: %5r amps' % r2.current)


class BoundedRegistance(Register):
	def __init__(self,ohms):
		super().__init__(ohms)

	@property
	def ohms(self):
		return self.ohms

	@ohms.setter
	def ohms(self,ohms):
		if ohms <=0:
			raise ValueError('%f ohms must be > 0 ' %ohms)

# r3 = BoundedRegistance(1e3)
# r3.ohms = 0

# ValueError: 0.000000 ohms must be > 0

class FixedRegistance(Register):
	def __init__(self,ohms):
		super().__init__(ohms)

	@property
	def ohms(self):
		return self._ohms

	@ohms.setter
	def ohms(self,ohms):
		if hasattr(self,'_ohms'):
			raise AttributeError("Can't set attibute")

r4 = FixedRegistance(1e3)
r4.ohms = 2e3



