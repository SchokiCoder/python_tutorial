# Conditions are a useful tool to control the flow of the script.
# Every script runs from top to bottom.

# Thats boring, let's change that.

num = 1

if (num == 0):
	print("zero")
	
elif (num == 1):
	print("one")
	
elif (num == 2):
	print("two")
	
else:
	print("other")

# If asks you to give it a 'True' value.
# The operators for comparisons give a True or False.
print(1 == 1)
print(2 == 1)

# When the If part does not run it goes to the elif,
# which asks an alternative question.
# You can chain as many 'elif's onto your 'if' as you like.
# Lastly you can put an 'else' to express the "all else failed" case.

# Also other comparison operators:
print("equal: ", 1 == 1)
print("lower than: ", 3 < 2)
print("greater than: ", 33 > 3)
print("lower or equal: ", 3 <= 3)
print("greater or equal: ", 4 >= 5)
print("not equal: ", 1 != 2)

# In one 'if' you can also cover multiple cases
if (1 == 1 and 2 > 1):
	print("The world still works.")
else:
	print("I don't feel well")

if (2 != 2 or 4 > 5):
	print("Oh god it looks bad.")
else:
	print("Yup, all right.")
