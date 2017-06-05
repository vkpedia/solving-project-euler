# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 21 (https://projecteuler.net/problem=21)

import math


def all_proper_divisors(n):
    divisors = [1]
    for i in range(2, 1 + int(math.sqrt(n))):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)

    return divisors


result = 0
for i in range(2, 10000):
    sum_of_divisors = sum(all_proper_divisors(i))
    if i != sum_of_divisors and sum(all_proper_divisors(sum_of_divisors)) == i:
        result += i

print(result)
