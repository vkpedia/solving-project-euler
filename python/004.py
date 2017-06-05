# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 4 (https://projecteuler.net/problem=4)

max_prod = 0

for a in range(100, 1000):
    for b in range(110, a, 11):
        product = a * b
        if (str(product) == str(product)[::-1]) and product > max_prod:
            max_prod = product

print(max_prod)
