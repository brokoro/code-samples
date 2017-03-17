import re

# Print directory of re module
print dir(re)

# Print a sorted list of all functions of the re module
# which contain the word 'find'
print sorted([f for f in dir(re) if 'find' in f])