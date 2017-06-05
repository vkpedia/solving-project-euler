# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 47 (https://projecteuler.net/problem=47)

upper_limit = 1000000
factors_list = [0] * upper_limit

for i, j in enumerate(factors_list):
    if i in [0, 1]:
        continue
    if factors_list[i] == 0:
        for k in range(i, upper_limit, i):
            factors_list[k] += 1
    if factors_list[i] == 4:
        if factors_list[i - 1] == factors_list[i - 2] == factors_list[i - 3] == 4:
            print(i - 3)
            break
