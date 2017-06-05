# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 9 (https://projecteuler.net/problem=9)

import math


def all_factors(n):
    factors = [1, n]
    for i in range(2, 1 + int(math.sqrt(n))):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)

    return sorted(factors)


# a + b + c = 1000; set limit = 1000
# a^2 + b^2 = c^2
# a = m^2 - n^2; b = 2*m*n; c = m^2 + n^2
# find a pair (m, n), such that m(m+n) = limit/2

limit = 1000
i = -1
factors = all_factors(limit // 2)
num_factors = len(factors)

while True:
    i += 1
    m_plus_n = factors[num_factors - 1 - i]
    m = factors[i]
    n = m_plus_n - m

    if m >= m_plus_n:
        break
    if m > n:
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        print(a * b * c)
