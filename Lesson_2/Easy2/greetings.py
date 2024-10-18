# Greet a user. If there is an exclamation point at the end of the input, 
# print out the greeting in all caps

name = input('What is your name? ')

if name[-1] == '!':
    print(f'Hello {name} Why are we yelling?'.upper())
else:
    print(f'Hello {name}.')