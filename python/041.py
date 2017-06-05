# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 41 (https://projecteuler.net/problem=41)

from itertools import permutations

from commons_euler import is_prime

digits = ['9', '8', '7', '6', '5', '4', '3', '2', '1']


def get_largest_pandigital_prime():
    for i in range(9):
        p = sorted(list(permutations(digits[i:9])), reverse=True)

        for item in p:
            if is_prime(int(''.join(item))):
                return ''.join(item)


print(get_largest_pandigital_prime())
