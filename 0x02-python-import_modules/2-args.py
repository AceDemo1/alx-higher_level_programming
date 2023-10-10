#!/usr/bin/python3
from sys import argv

# Remove the script name from the arguments
args = argv[1:]

# Get the number of arguments
num_args = len(args)

# Print the number of arguments
print("{} argument{}:".format(num_args, 's' if num_args != 1 else ''), end='')

# Print a period if there are no arguments
if num_args == 0:
    print('.')
else:
    print('')

# Print the list of arguments
for i, arg in enumerate(args, 1):
    print("{}: {}".format(i, arg))

