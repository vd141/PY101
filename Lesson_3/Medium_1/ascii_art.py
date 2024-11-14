'''
prints out string10 times with each line prefixed by one more hyphen than the
line above it
'''

REPEATED_STRING = 'The Flintstones Rock!'

for i in range(1,11):
    print(f'{'-' * i}{REPEATED_STRING}')
