# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 22 (https://projecteuler.net/problem=22)

f = open('p022_names.txt')
names = sorted(f.read().replace('"', '').split(','))

total = 0
for pos, name in enumerate(names):
    total += (pos + 1) * sum([ord(c) - 64 for c in name])

print(total)
