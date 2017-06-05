# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 1 (https://projecteuler.net/problem=1)

def sum_to_n(n):
    n = int(n)
    return n * (n + 1) // 2


n = 999
# Add the sum of the multiples of 3 and 5, and subtract the sum of multiples of 15
total = 3 * sum_to_n(n / 3) + 5 * sum_to_n(n / 5) - 15 * sum_to_n(n / 15)

print(total)
