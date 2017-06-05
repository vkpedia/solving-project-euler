# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 34 (https://projecteuler.net/problem=34)

from commons_euler import get_factorial


def is_curious_number(n):
    if n == sum([get_factorial(int(i)) for i in str(n)]):
        return True
    return False


factorials = {0: 1, 1: 1}
print(sum([i for i in range(3, 1000000) if is_curious_number(i)]))
