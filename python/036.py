# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 36 (https://projecteuler.net/problem=36)

def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


print(sum([i for i in range(1, 1000000, 2) if is_palindrome(i)
           and is_palindrome(str(bin(i)).replace('0b', ''))]))
