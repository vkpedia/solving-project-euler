# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 45 (https://projecteuler.net/problem=45)

from math import sqrt

i = 286

while True:
    t = i * (i + 1) // 2
    p = (1 + sqrt(1 + 24 * t)) / 6
    h = (1 + sqrt(1 + 8 * t)) / 4

    if p == int(p) and h == int(h):
        print(t)
        break
    i += 1
