class A(object):
	"""docstring for A"""
	def __init__(self):
		print("A")
		super(A, self).__init__()

ins_a = A()
print(ins_a.__dict__)
print(ins_a.__class__)