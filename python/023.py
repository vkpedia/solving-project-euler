# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 23 (https://projecteuler.net/problem=23)

from commons_euler import all_proper_divisors

abundant_numbers = set()
for i in range(12, 28124):
    if sum(all_proper_divisors(i)) > i:
        abundant_numbers.add(i)

abundant_numbers_sum = set()
for number1 in abundant_numbers:
    for number2 in abundant_numbers:
        abundant_numbers_sum.add(number1 + number2)

result = 0
for i in range(1, 28124):
    if i not in abundant_numbers_sum:
        result += i

print(result)
