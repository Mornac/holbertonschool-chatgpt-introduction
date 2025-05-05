#!/usr/bin/python3
import sys

/**
 *factorial(n) - calculate the factorial of a non-negative integer
 *using recursion
 *@n (int): the non-negative integer for which to calcultate the factorial
 *Return: int the factorial of the input number
 */
 def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
