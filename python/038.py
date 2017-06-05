# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 38 (https://projecteuler.net/problem=38)

digits = [str(i) for i in range(1, 10)]
max_concat_product = 0

for i in range(1, 10000):
    concat_product = ''
    for j in range(1, 10):
        product = str(i * j)
        concat_product += product
        if len(concat_product) == 9 and sorted(concat_product) == digits:
            max_concat_product = max(max_concat_product, int(concat_product))

print(max_concat_product)
