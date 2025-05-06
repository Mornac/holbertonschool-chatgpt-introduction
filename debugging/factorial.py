#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        # Erreur ici : il manque 'n -= 1', ce qui rend la boucle infinie
    return result

print(factorial(int(sys.argv[1])))

