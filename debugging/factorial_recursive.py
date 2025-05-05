#!/usr/bin/python3
import sys

 def factorial(n):
     """
    Description:
    Calculate the factorial of a non-negative integer.

    Parameters:
    n (int): The integer for which to calculate the factorial.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
