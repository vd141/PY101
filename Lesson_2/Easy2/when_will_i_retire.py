# displays when user will retire and how many years to work until retirement
from datetime import datetime

current_year = datetime.today().year

current_age = int(input('What is your age? '))
retirement_age = int(input('At what age would you like to retire? '))
difference = retirement_age - current_age

print(f'It\'s {current_year}. You will retire in {difference + current_year}.')
print(f'You only have {difference} years of work to go!')