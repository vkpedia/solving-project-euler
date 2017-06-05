# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 40 (https://projecteuler.net/problem=40)

s = ''
p = 1

for i in range(1, 1000000):
    s += str(i)

for i in range(0, 7):
    p *= int(s[10 ** i - 1])
print(p)
