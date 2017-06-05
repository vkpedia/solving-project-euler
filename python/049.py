# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 49 (https://projecteuler.net/problem=49)

from itertools import permutations

from commons_euler import get_primes


def get_permutations(n):
    return list(filter(lambda a: a != n,
                       [int(''.join(x))
                        for x in list(permutations(list(str(n))))]))


def get_prime_permutations(primes):
    for i in primes:
        result = list(set([x for x in get_permutations(i) if x in primes]))

        if len(result) == 3:
            result = sorted(result)
            if result[2] - result[1] == result[1] - result[0]:
                return result


def get_four_digit_primes():
    primes = [i for i in get_primes(10000)
              if i > 1000 and i not in [1487, 4817, 8147]]

    return primes


result = get_prime_permutations(get_four_digit_primes())
print(str(result[0]) + str(result[1]) + str(result[2]))
