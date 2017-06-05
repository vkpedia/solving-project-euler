# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 7 (https://projecteuler.net/problem=7)

from commons_euler import is_prime

count = 3
i = 7

while count < 10001:
    if i % 10 in [1, 3, 7, 9] and is_prime(i):
        count += 1

    i += 1
print(i - 1)
