# How big is the room?
# Build a program that asks the user to enter the length and width of a room, in
# meters, then prints the room's area in both square meters and square feet
# 
# 1 sq. meter == 10.7639 sq. feet

SQUAREFEET = 10.7639

length = int(input('Please provide the length of the room in meters: '))
width = int(input('Please provide the width of the room in meters: '))

print(f'The room\'s area is {length * width} meters squared and '
      f'{length * width * SQUAREFEET} feet squared.')