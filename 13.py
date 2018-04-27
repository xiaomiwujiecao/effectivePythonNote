#encoding=utf-8
import json

handle = open('/tmp/random_data.txt')
try:
	data = handle.read()
finally:
	handle.close()

def load_json_key	(data,key):
	try:
		result_dict = json.loads(data)
	except ValueError as e:
		raise KeyError from e
	else:
		return result_dict[key]

UNDEFINED = object()
def divide_json(path):
	handle = open(path,'r+')
	try:
		data = handle.read()
		op = json.loads(data)
		value = (
			op['numerator']/
			op['denominator']
		)
	except 	ZeroDivisionError as e:
		return UNDEFINED
	else:
		op['result'] = value
		result = json.dump(op)
		handle.seek(0)
		handle.write(result)
		return value
	finally:
		handle.close()
