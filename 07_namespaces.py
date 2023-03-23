# Namespaces limit the accessibility of variables and other symbols.
def my_func():
	a: int = 0
	
	a += 2
	
	print(a == 3)

# The variable 'a' is not accessable from out here.
# This script fails here, saying that 'a' is not defined.
print(a)
