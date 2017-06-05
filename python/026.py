# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 26 (https://projecteuler.net/problem=26)

from commons_euler import is_prime


def get_cycle_length(n):
    dividend = 1
    divisor = n
    remainders = {}
    position = 0

    while dividend not in remainders:
        remainders[dividend] = position
        dividend = dividend * 10 % divisor
        position += 1
    return position - remainders[dividend]


reciprocal_cycle_lengths = {}

for i in range(2, 1000):
    if is_prime(i):
        reciprocal_cycle_lengths[i] = get_cycle_length(i)

print(max(reciprocal_cycle_lengths, key=reciprocal_cycle_lengths.get))
