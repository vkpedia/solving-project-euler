# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 17 (https://projecteuler.net/problem=17)

d = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
     6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
     12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
     17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
     30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
     80: 'eighty', 90: 'ninety'}

s = 0
for i in range(1,1000):
    hundreds = i // 100
    if hundreds != 0:
        s += len(d[hundreds]) + 7 # add 7 for the word "hundred"
        if i % 100 > 0:
            s += 3 # add 3 for the word "and" but only if the number is not a multiple of 100

    i %= 100 # check the tens digit
    if i > 20: # if the number is greater than 20, get the tens digit
        tens = i - (i%10)
        s += len(d[tens])
        i %= 10 # get the units digit

    s += len(d[i])

print(s + len('onethousand'))