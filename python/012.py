# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 12 (https://projecteuler.net/problem=12)

from commons_euler import all_factors

i = 0
while True:
    i += 1
    triangle_num = i * (i + 1) // 2
    if len(all_factors(triangle_num)) > 500:
        print(triangle_num)
        break
