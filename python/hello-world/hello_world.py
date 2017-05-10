#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if len(name) >= 1:
        greeting = "Hello," + " " +name+ "!"
    else:
        greeting = "Hello, World!"
    return greeting
