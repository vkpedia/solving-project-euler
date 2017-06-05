# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 28 (https://projecteuler.net/problem=28)

sum = 1
for i in range(3, 1002, 2):
    top_right = i ** 2
    for j in range(4):
        sum += top_right - j * (i - 1)
print(sum)
