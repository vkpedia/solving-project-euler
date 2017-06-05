# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 25 (https://projecteuler.net/problem=25)

a = 1
b = 1
i = 2

while True:
    a, b = b, a + b
    i += 1
    if len(str(b)) == 1000:
        break

print(i)
