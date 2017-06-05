# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 39 (https://projecteuler.net/problem=39)

from math import sqrt

p = {}

for a in range(1, 500):
    for b in range(a + 1, 500):
        c = sqrt(a ** 2 + b ** 2)
        if int(c) == c:
            if a + b + c > 1000:
                continue
            if a + b + c in p:
                p[a + b + c] += 1
            else:
                p[a + b + c] = 1

print(int(max(p, key=p.get)))
