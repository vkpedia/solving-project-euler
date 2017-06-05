# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 15 (https://projecteuler.net/problem=15)

# In a 2 x 2 grid, to get from the top-left to the bottom-right,
# we have to make 2 moves down and 2 moves right for a total of 4 moves
# The order of making these moves does not matter.
# We can make 4 moves in 4! ways. We can make the two moves in 2! ways
# So the total number of ways is 4! / (2! * 2!)
# Which the formula for nCr, which is n! / (r! * (n-r)!)

def factorial(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


print(factorial(40) // (factorial(20) ** 2))
