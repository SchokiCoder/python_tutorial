# Python can import someone elses work, you lazy bum.
import importme

importme.add(1, 1)

# You can also type:
from importme import sub

sub(3, 2)

# so you can save your fingers from typing the modules name every time.
# Just watch out for name collisions.
# They happen, if for example we already would have had a function called 'sub'.
