# How old is Teddy?
from random import randint

def teddy_random_age():
    name = input('What is the person\'s name? ')
    if not name:
        print(f'Teddy is {randint(20,100)} years old!')
    else:
        print(f'{name} is {randint(20,100)} years old!')

teddy_random_age()