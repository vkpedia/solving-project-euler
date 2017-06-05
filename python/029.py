# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 29 (https://projecteuler.net/problem=29)

result_set = set()

for a in range(2, 101):
    for b in range(2, 101):
        result_set.add(a ** b)

print(len(result_set))
