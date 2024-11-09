def twice(number):
    '''
    write a function that returns the number provided as an argument multiplied by 
    two, unless the argument is a double number. if the argument is a double number,
    return the double number as-is
    '''
    number_str = str(number)

    # double numbers can only have an even length
    # check if number is an even length
    # if so, check to see that the first half of the string matches the second 
    # half of the string
    # if it does, return the double number,
    # if it doesn't multiply it by two

    if len(number_str) % 2 == 0:
        midpoint = int(len(number_str) / 2)
        if number_str[:midpoint] == number_str[midpoint:]:
            return number
        else:
            return number * 2
    else:
        return number * 2
    

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
