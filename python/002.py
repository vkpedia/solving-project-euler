# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 2 (https://projecteuler.net/problem=2)

n = 4000000
total = 0

# Let a, b, and c be represent the first three numbers. We will compute the
# sum of all c's under 4,000,000 to get the result
a = 1
b = 1
c = a + b

while c < n:
    total += (c)
    a = b + c
    b = c + a
    c = a + b

print(total)
