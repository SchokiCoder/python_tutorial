# This is a Python comment as such,
# these lines are ignored by the Python parser.

# Python scripts run immediately, no main function needed.

# This:
myvar = 34
# is a variable.

# Variables are for storing results of calculations.

# In Python variables are created the moment you mention them.
# In other languages like C variables need to be declared first but not here.
# In Python, variables are flexible in type.
stringvar = "my string"
stringvar = 55

# Python has type hints.
# They don't hold you from reassigning a value of completely different type.
stringvar: str = "1 string"
stringvar = 666

# But they are useful with linters.
# Linters are programs that scan your source code
# and warn you about your mistakes.
# On such program would be pylint for example.
# Available via pip or many Linux package managers.
# run in terminal: pip install pylint
#
# pylint will detect many things as wrong in this tutorial,
# because so far this is only for explanation.
# I will demonstrate a proper pylint-approved file later.

# Constants can be a handy tool to reference an often used value,
# that you know will not change.
# Python technically also does not have constants.
#
# However the consensus seems to be that if a variable is defined outside of
# any funtion it is a constant and constants should have upper case names.

MY_CONST = 43 # ok
my_var = "hi" # bad

# Functions will be explained later.
