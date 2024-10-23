# What century is that?


def century(year):
    century = -(-year // 100) # ceiling division

    str_century = str(century)

    # if century has 2 or more digits, check to see if the last two digits are
    # in the teens. if they are, use teenth endings. else, use

    return f'{str_century}{suffix(str_century)}'

def suffix(century_str):
    if len(century_str) >= 2:
        if century_str[-2] == '1':
            return 'th'
    match century_str[-1]:
        case '0':
            return 'th'
        case '1':
            return 'st'
        case '2':
            return 'nd'
        case '3':
            return 'rd'
        case _:
            return 'th'

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True