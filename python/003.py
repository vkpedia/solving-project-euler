# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 3 (https://projecteuler.net/problem=3)

from commons_euler import is_prime


def largest_prime_factor(n):
    i = 2
    while n > i:
        if n % i == 0 and is_prime(i):
            n = n // i
        i += 1
    return n


print(largest_prime_factor(600851475143))
