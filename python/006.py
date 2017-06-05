# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 6 (https://projecteuler.net/problem=6)

n = 100
sum = n * (n + 1) // 2
sum_of_squares = n * (n + 1) * (2 * n + 1) // 6

print(sum ** 2 - sum_of_squares)
