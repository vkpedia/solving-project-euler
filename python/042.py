# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 42 (https://projecteuler.net/problem=42)

f = open('p042_words.txt')
words = f.read().replace('"', '').split(',')

triangle_numbers = {i * (i + 1) // 2 for i in range(1, 34)}

result = 0
for word in words:
    word_sum = 0
    for char in word:
        word_sum += ord(char) - 64
    if word_sum in triangle_numbers:
        result += 1

print(result)
