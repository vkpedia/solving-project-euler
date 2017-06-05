# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 44 (https://projecteuler.net/problem=44)

p = set([n * (3 * n - 1) // 2 for n in range(1, 2500)])

print(min([i - j for j in p for i in p
           if i > j and i + j in p and i - j in p]))
