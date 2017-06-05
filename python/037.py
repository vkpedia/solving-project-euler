# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 37 (https://projecteuler.net/problem=37)

from commons_euler import is_prime


def is_truncatable(n):
    n_str = str(n)

    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:len(n_str)])):
            return False
        if not is_prime(int(n_str[0:len(n_str) - i])):
            return False
    return True


count = 0
total = 0
n = 13

while count != 11:
    if is_prime(n) and is_truncatable(n):
        count += 1
        total += n
    n += 1

print(total)
