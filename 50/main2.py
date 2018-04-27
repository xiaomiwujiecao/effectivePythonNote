from analysis.utils import inspect

from frontend.utils import inspect


def determine_weight(volume,desity):
	if desity <=0:
		raise ValueError('Desiny must be positive')

