# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 35 (https://projecteuler.net/problem=35)

from commons_euler import get_primes


def is_circular(n):
    str_n = str(n)

    for i in range(len(str_n)):
        if int(str_n[i:] + str_n[:i]) not in primes:
            return False
    return True


n = 1000000
chars = ('0', '2', '4', '5', '6', '8')

primes = get_primes(n)
new_primes = set([2, 5])

for i in primes:
    has_char = False
    if i not in [2, 5]:
        for c in chars:
            if c in str(i):
                has_char = True
                break
        if not has_char:
            new_primes.add(i)

print(sum([1 for i in new_primes if is_circular(i)]))
