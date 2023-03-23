# A loop: to repeat, to repeat, to repeat, to repeat, to repeat, to repeat, ...
# some code.

i = 0

while (i < 10):
	print("i: ", i)
	i += 1

# As long as that condition in the header is True, it will run... forever.
# Make sure that the condition is eventually not 'True' anymore.

# Attention: new type ahead, array.
# Arrays hold many values at once.

my_arr = [1, 2, 3, 5, 8, 13, 21]

# The following loop runs once for each element of the array.
# Every time it loads a new value from 'my_arr' into the variable 'item'.

for item in my_arr:
	print("fib item: ", item)

# To write this manually, it would kinda look like this:

i = 0

while (i < len(my_arr)):
	print("fib iter: ", my_arr[i])
	i += 1

# So it saves you some time and is less error prone.
# (You could forget the i += 1)
# By the way with these -> [], you access the array.
# In Python the first element of the array is accessible via a 0.

# Loops also have some control flow:
i = 0

while (True):
	if (i > 10):
		break
	
	i += 1
	
	if (i == 10):
		continue
		
	print("control the loop, ", i)

# 'break' stops the loop altogether.
# 'continue' skips to the next run of the loop.
