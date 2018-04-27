# encoding=utf-8
def remainder(number, divisor):
	return number % divisor


assert remainder(20, 7) == 6


def flow_rate(weight_diff, time_diff):
	return weight_diff / time_diff


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print('%.3f kg per second' % flow)


# scaling factor

def flow_rate2(weight_diff, time_diff, period=1):
	return (weight_diff / time_diff) * period


def flow_rate3(weight_diff, time_diff, peroid=1, units_per_kg=1):
	return ((weight_diff * units_per_kg) / time_diff) * peroid


