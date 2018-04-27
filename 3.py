#encoding-utf-8
# 字符顺序  python3 byte str
# 字符顺序 python2 str unicode
# python3 str = python2 unicode  = 8位
'''
unicode字符串转换为二进制 encode
二进制转换为unicode字符换 decode
'''

# helper func

# python3 总返回  str
import os


def to_str(byte_or_str):
	if isinstance(byte_or_str,bytes):
		value = byte_or_str.decode('utf-8')
	else:
		value = byte_or_str
	return value

def to_bytes(byte_or_str):
	if isinstance(byte_or_str,str):
		value = byte_or_str.encode('utf-8')
	else:
		value = byte_or_str
	return value
# python2 总返回 unicode

# python2
'''
def python2_to_str(unicode_or_str):
	if isinstance(unicode_or_str,unicode):
		value = unicode_or_str.encode('utf-8')
	else:
		value = unicode_or_str
	return value
'''


# 格式字符串中 可以使用 '%s 等形式来代表Unicode'

#

with open('/tmp/random.bin','wb') as f:
	f.write(os.urandom(10))