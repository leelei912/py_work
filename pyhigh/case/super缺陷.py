class A(object):
	"""docstring for A"""
	def __init__(self):
		print('A')
		super(A, self).__init__()

class B(object):
	"""docstring for B"""
	def __init__(self):
		print("B")
		super(B, self).__init__()

class C(A,B):
	"""docstring for C"""
	def __init__(self):
		print("C")
		A.__init__(self)
		B.__init__(self)


print("MRO:",[x.__name__ for x in C.__mro__])
C()#CABB super(A,self).__init__()将调用B的构造程序,因为根据MRO的顺序，super C应该是B
	

		