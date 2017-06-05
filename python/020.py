# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 20 (https://projecteuler.net/problem=20)

from commons_euler import get_factorial

print(sum(int(i) for i in str(get_factorial(100))))
