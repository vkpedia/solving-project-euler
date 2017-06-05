# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 33 (https://projecteuler.net/problem=33)

from math import gcd


def get_common_digit(i, j):
    for x in str(i):
        for y in str(j):
            if x == y:
                return int(x)
    return -1


def get_num_sans_digit(number, digit):
    return int(str(number).replace(str(digit), '', 1))


product_num = 1
product_den = 1

for i in range(11, 98):
    for j in range(i + 1, 99):
        if i % 10 == 0 and j % 10 == 0:
            continue
        d = get_common_digit(i, j)
        if d != -1:
            try:
                if i / j == get_num_sans_digit(i, d) / get_num_sans_digit(j, d):
                    product_num *= i
                    product_den *= j
            except ZeroDivisionError:
                pass

print(product_den // gcd(product_num, product_den))
