# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 5 (https://projecteuler.net/problem=5)

def gcd(a, b):
    x = max(a, b)
    y = min(a, b)

    while x % y != 0:
        z = x % y
        x = max(y, z)
        y = min(y, z)

    return y


product = 1
for i in range(1, 21):
    product = product * i // gcd(product, i)

print(product)
