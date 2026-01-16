# unlike comments python does not ignores docstrings.
def square(n):
    '''takes the no. n and returns the square of that number'''
    print(n**2)
square(7)
print(square.__doc__)

# docstring just comes below the function header and is enclosed in triple brackets.
# docstrings can be accessed using __doc__ attribute of the function.
import this
print(this.__doc__)
# this is a module that contains the zen of python as its docstring.

    