# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 10 (https://projecteuler.net/problem=10)

# Sieve of Eratosthenes
upper_limit = 2000000
primes_list = [True] * upper_limit
primes_list[0] = False
primes_list[1] = False
sum = 0

for i in range(2, upper_limit):
    if primes_list[i]:
        sum += i
        for j in range(i * i, upper_limit, i):
            primes_list[j] = False

print(sum)
