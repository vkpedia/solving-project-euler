# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 31 (https://projecteuler.net/problem=31)

total = 200
coins = sorted([1, 2, 5, 10, 20, 50, 100, 200], reverse=True)
count = 0

for a in range(total, -1, -coins[0]):
    for b in range(a, -1, -coins[1]):
        for c in range(b, -1, -coins[2]):
            for d in range(c, -1, -coins[3]):
                for e in range(d, -1, -coins[4]):
                    for f in range(e, -1, -coins[5]):
                        for g in range(f, -1, -coins[6]):
                            count += 1

print(count)
