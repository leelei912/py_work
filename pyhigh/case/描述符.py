class UpperString(object):
	"""docstring for UpperString"""
	def __init__(self):
		self._value = ''

	def __get__(self, instance, klass):
		return self._value

	def __set__(self, instance, value):
		self._value = value.upper()

class MyDesc(object):
	"""docstring for UpperString"""
	def __init__(self):
		self._value = ''

	def __get__(self, instance, klass):
		return self._value

	def __set__(self, instance, value):
		self._value = value.upper()

class MyClass(object):
	attribute = UpperString()

ins = MyClass()
print(ins.attribute)#空行

ins.attribute = "my value"
print(ins.attribute)#转换成大写

ins.__dict__ = {}

ins.new_attr = 1
print(ins.__dict__)#{'new_attr':1}

MyClass.new_attr = MyDesc()
print(ins.__dict__)#{'new_attr':1}

print(ins.new_attr)#空行

ins.new_attr = "other Value"
print(ins.new_attr)#大写

print(ins.__dict__)#空行

