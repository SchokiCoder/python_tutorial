# Here we have a data bundle also called class or struct.
# It has two variables in this context called members
# and a function in this context called method.
class SomeData:
	a: int
	b: int
	
	def __init__(self):
		self.a = 0
		self.b = 0
	
	def status(self):
		print("SomeData: a " + str(self.a) + ", b " + str(self.b))

# This here calls the __init__ function on a new instance of SomeData.
my_data = SomeData()

# From now on you can use it's members and methods.
# With the little point you can access the struct's members and methods.
my_data.a = 1
my_data.status()
