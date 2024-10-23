# How big is the room?
# Build a program that asks the user to enter the length and width of a room, in
# meters, then prints the room's area in both square meters and square feet
#
# Answer can go to the nearest hundredth after the decimal
# 
# 1 sq. meter == 10.7639 sq. feet

SQ_FEET_PER_SQ_M = 10.7639

unit = 'a'

while unit not in 'mf':
    length = float(input('Please enter the length of the room in meters: '))
    width = float(input('Please enter the width of the room in meters: '))
    unit = input('Please specify whether the output units will be in square m'
                ' or square ft. m or f? ')

    area = length * width
    sqft_area = area * SQ_FEET_PER_SQ_M

    if unit == 'm':
        print(f'The room\'s area in square meters is {area:.2f}.')
    elif unit == 'f':
        print(f'The room\'s area in square feet is {sqft_area:.2f}.')
    else:
        print('Please enter either f or m next time.')