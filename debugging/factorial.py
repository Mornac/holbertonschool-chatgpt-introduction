#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémentation nécessaire
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <number>")
    else:
        try:
            num = int(sys.argv[1])
            if num < 0:
                print("Le factoriel n'est pas défini pour les entiers négatifs.")
            else:
                f = factorial(num)
                print(f)
        except ValueError:
            print("Veuillez entrer un entier valide.")

