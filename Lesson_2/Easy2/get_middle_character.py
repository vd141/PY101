# Get Middle Character
#

def center_of(string):
    str_len = len(string)
    midpoint = str_len // 2
    # len of 3, middle character is index of 1 (3//2 == 1)
    # len of 4, middle character is 1 and 2 (4 // 2 == 2)

    return (string[midpoint] if str_len % 2 != 0 else 
            string[midpoint - 1:midpoint + 1])

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True