# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 43 (https://projecteuler.net/problem=43)

from itertools import permutations

digits = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']

numbers = list(permutations(digits))
total = 0

for number in numbers:
    n = ''.join(number)
    if int(n[7:10]) % 17 == 0 and int(n[6:9]) % 13 == 0 and int(n[5:8]) % 11 == 0:
        if int(n[4:7]) % 7 == 0 and int(n[3:6]) % 5 == 0:
            if int(n[2:5]) % 3 == 0 and int(n[1:4]) % 2 == 0:
                total += int(n)

print(total)
