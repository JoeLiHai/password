def leap_y(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

print(leap_y(2024))
print(is_leap(2024))