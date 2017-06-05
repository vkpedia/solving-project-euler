# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 24 (https://projecteuler.net/problem=24)

import itertools

result = list(itertools.permutations(list(range(10))))[999999]
print(''.join([str(c) for c in result]))
