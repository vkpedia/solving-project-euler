# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 46 (https://projecteuler.net/problem=46)

from math import sqrt

from commons_euler import get_primes

upper_limit = 100000

# We can exclude 2 from primes as only odd primes will fit the solution
primes = [i for i in get_primes(upper_limit) if i > 2]

# We can ignore numbers <= 33, from the problem statement
odd_composites = sorted([i for i in range(upper_limit)
                         if i % 2 == 1 and i >= 35 and i not in primes])

for number in odd_composites:
    test_primes = [i for i in primes if i < number]
    conjecture = True
    for prime in test_primes:
        diff = number - prime
        if sqrt(diff // 2) == int(sqrt(diff // 2)):
            conjecture = True
            break
        else:
            conjecture = False

    if not conjecture:
        print(number)
        break
