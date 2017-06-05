from math import sqrt


def is_prime(n=1):
    if n < 2:
        return False
    for i in range(2, 1 + int(sqrt(n))):
        if n % i == 0:
            return False
    return True


def get_primes(n=1000000):
    upper_limit = n
    primes_list = [True] * upper_limit
    primes_list[0] = False
    primes_list[1] = False

    for i in range(2, upper_limit):
        if primes_list[i]:
            for j in range(i * i, upper_limit, i):
                primes_list[j] = False

    return [i for i, j in enumerate(primes_list) if j]
