# Functions are subroutines.
# Here we declare a function that takes one boolean and prints it.
# After that it returns 0.
def my_subr(the_bool: bool) -> int:
	print("1 bool: ", the_bool)
	return 0

# A function begins with that first 'def' line
# and goes for as long as you keep up the indentation.
#
# In Python you can not just put the begin of your lines where ever you want.
# The indentation is significant.

ret = my_subr(False)
print(ret)
