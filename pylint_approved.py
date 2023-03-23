#!/bin/python3
"""Asks for a number and returns the nth fibonacci number"""

# Above is a shebang line and a module documentation string (doc string).
#
# The first line (the shebang line) says which interpreter should be used for
# this file.
# This is important in many UNIX-like systems and Linux.
# Thanks to the shebang line, the file can be run by typing:
# ./pylint_approved.py
#
# The second line (the doc string line) just documents what the purpose of this
# file is.
# They are usually given as a multiline string (by using three " characters).
# They also work for functions.

DE_GREET = "Die wie vielte Fibonacci Nummer ist erfragt?"
EN_GREET = "Which iteration of a fibonacci number is wished for?"

def fib(nth: int) -> int:
    """Returns the nth fibonacci number"""
    i: int = 0
    f_a: int = 0
    f_b: int = 1
    f_c: int = 1

    while i < nth:
        f_a = f_b
        f_b = f_c
        f_c = f_a + f_b
        i += 1

    return f_a


# Now here is a common practice.
# We will check if the current file is the file that had been opened by parser
# as the first or "main" file.

if __name__ == "__main__":
    lang = input("Choose your language (de/en): ")

    if lang == "de":
        print(DE_GREET)
    else:
        print(EN_GREET)

    n = int(input())

    print(str(fib(n)))

# Other minor changes to appease pylint include:
# - the use of 4 spaces instead of a tab for indentation
# - not using numbers at beginning of the filename because of snake_case names
