# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 32 (https://projecteuler.net/problem=32)

from math import sqrt

pandigital_list = list('123456789')


def is_pandigital_product(n):
    for i in range(2, 1 + int(sqrt(n))):
        if n % i == 0:
            if sorted(list(str(n)) + list(str(i)) + list(str(n // i))) == pandigital_list:
                return True
    return False


print(sum([i for i in range(4000, 75000) if is_pandigital_product(i)]))
