# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Common functions used across multiple solutions

from math import sqrt


def is_prime(n=1):
    """
    Given a number, returns True if number is prime, False if not.
    All numbers less than 2 are considered non-prime.
    Non-integers are considered non-prime.

    Args:
        param n: assumed to be an integer

    Returns:
        True if n is prime, False if not

    Raises:
        AssertionError: If n is not an integer
    """
    assert isinstance(n, int)
    if n < 2:
        return False
    for i in range(2, 1 + int(sqrt(n))):
        if n % i == 0:
            return False
    return True


def get_primes(n=1000000):
    """
    Uses the Sieve of Eratosthenes to return all primes upto a given limit
    The upper limit is excluded from the returned list

    Args:
        param n: assumed to be an integer

    Returns:
        List of prime numbers up to, but not including, the upper limit

    Raises:
        AssertionError: If n is not an integer
    """
    assert isinstance(n, int)
    upper_limit = n
    primes_list = [True] * upper_limit
    primes_list[0] = False
    primes_list[1] = False

    for i in range(2, upper_limit):
        if primes_list[i]:
            for j in range(i * i, upper_limit, i):
                primes_list[j] = False

    return [i for i, j in enumerate(primes_list) if j]


def all_factors(n):
    """
    Returns all factors of an integer n, by repeated division

    Args:
        param n: assumed to be an integer

    Returns:
        List of factors of the numbers

    Raises:
        AssertionError: If n is not an integer
    """
    assert isinstance(n, int)
    factors = [1, n]
    for i in range(2, 1 + int(sqrt(n))):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)

    return factors


def get_factorial(n):
    """
        Returns factorial of a positive integer n, defined as n * n-1 * ... * 1

        Args:
            param n: assumed to be an integer

        Returns:
            Factorial of n

        Raises:
            AssertionError: If n is not an integer
    """
    assert isinstance(n, int)
    assert n >= 0
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


def all_proper_divisors(n):
    """
        Returns all proper divisors of a number, i.e. any integer > 0
        that divides the number without leaving a remainder

        Args:
            param n: assumed to be a positive integer

        Returns:
            List of proper divisors

        Raises:
            AssertionError: If n is not an integer
    """
    assert isinstance(n, int)
    assert n > 0
    divisors = {1}
    for i in range(2, 1 + int(sqrt(n))):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    return divisors
