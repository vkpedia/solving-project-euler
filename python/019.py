# Solving Project Euler (http://www.vijayn.com/projects/solving-project-euler
#
# Problem 19 (https://projecteuler.net/problem=19)

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


month_offset = {1: 1, 2: 4, 3: 4, 4: 0, 5: 2, 6: 5, 7: 0,
                8: 3, 9: 6, 10: 1, 11: 4, 12: 6}

# days = {5: 'Monday', 6: 'Tuesday', 0: 'Wednesday', 1: 'Thursday',
#         2: 'Friday', 3: 'Saturday', 4: 'Sunday'}

sundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        day = 1 + year + month_offset[month]
        if is_leap_year(year) and month > 2:
            day += 1
        if is_leap_year(year - 1):
            day += (year - 1901) // 4
        if day % 7 == 4:
            sundays += 1

print(sundays)
