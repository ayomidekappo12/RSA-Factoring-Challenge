#!/usr/bin/python3
import sys
from ecm import *

if len(sys.argv) < 2:
    print("Usage: rsa <file>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename) as f:
    n = int(f.readline().strip())

factors = ecm.factor(n)

if factors is None:
    print("Unable to find prime factors")
else:
    p, q = factors
    print(f"{n}={p}*{q}")
