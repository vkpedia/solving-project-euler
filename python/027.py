# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 27 (https://projecteuler.net/problem=27)

# n^2 + an + b
# |a| < 1000 => a = -999...999
# |b| <= 1000 => b = -1000...1000
from commons_euler import is_prime

result_set = {}
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        if not is_prime(b):
            continue
        n = 0
        count = 0
        while True:
            number = n ** 2 + a * n + b
            if not is_prime(number):
                break
            count += 1
            n += 1
        result_set[(a, b)] = count

a, b = max(result_set, key=result_set.get)
print(a * b)
