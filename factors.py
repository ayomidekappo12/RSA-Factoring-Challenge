#!/usr/bin/python3
import sys

def factorize(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return (i, n//i)
    return None

if len(sys.argv) < 2:
    print("Usage: factors <file>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename) as f:
    for line in f:
        n = int(line.strip())
        factors = factorize(n)
        if factors is not None:
            p, q = factors
            print(f"{n}={p}*{q}")
