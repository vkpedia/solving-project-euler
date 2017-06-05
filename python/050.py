# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 50 (https://projecteuler.net/problem=50)

from commons_euler import get_primes

upper_limit = 1000000
primes = get_primes(upper_limit)
primes_set = set(primes)  # for quicker comparisons

total = 0
max_count = 0
result = 0

for i, j in enumerate(primes):
    total = j
    count = 1
    for k in range(i + 1, len(primes)):
        total += primes[k]
        count += 1
        if total >= upper_limit:
            break
        if total in primes_set and count > max_count:
            result = total
            max_count = count

print(result)
