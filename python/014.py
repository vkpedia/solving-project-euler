# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 14 (https://projecteuler.net/problem=14)

# The Collatz sequence for 2 is 2 -> 1; length = 2
# The Collatz sequence for 3 is 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# However, we don't need to get to 1, we can store the Collatz length for 2
# To do this, we will stored the lengths in a dictionary for easy reference
# When any sequence gets to 2, we can stop processing it, and merely add the Collatz length of 2 to it

collatz_lengths = {1: 1}


def get_collatz_length(n):
    curr_length = 1
    i = n

    while n != 1:
        if n in collatz_lengths:
            collatz_lengths[i] = curr_length + collatz_lengths[n] - 1
            return
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        curr_length += 1
    collatz_lengths[i] = curr_length


for i in range(2, 16):
    get_collatz_length(i)

print(max(collatz_lengths, key=collatz_lengths.get))
