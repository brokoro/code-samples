# Code snippets for learning lambda functions

# Define lambda function out which writes the string representation of the list
# of arguments. Ex, out(1, 2 [3, 4, 5]) should write 1, 2, [3, 4, 5]

import sys
out = lambda *x: sys.stdout.write(" ".join(map(str,x)))

from functional import seq

# map, filter, reduce sequence

reduce(lambda x, y: x*y, filter(lambda x: x>0, map(lambda x: x - 1, some_list)))

# Easily readible version

seq(some_list).map(lambda x: x -1, a).filter(lambda x: x>0).reduce(lambda x, y: x*y)
