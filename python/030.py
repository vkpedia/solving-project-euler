# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 30 (https://projecteuler.net/problem=30)

grand_total = 0
upper_bound = ((9 ** 5) * 6) + 1

for i in range(2, upper_bound):
    j = str(i)
    total = 0
    for x in j:
        total += int(x) ** 5
    if total == i:
        grand_total += i
print(grand_total)
