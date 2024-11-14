'''
1. The user makes a choice.
2. The computer makes a choice.
3. A winner is displayed.

add lizard and spock to the game
shortened input - first character of each option. because scissors and spock 
    both start with s, ask for two characters
best of five
pylint complaints
code review
'''

import random
import os
import time

VALID_CHOICES = {'r': 'rock',
                 'p': 'paper',
                 'sc': 'scissors',
                 'l': 'lizard',
                 'sp': 'spock',
                 }
VALID_CHOICES_SHORTCUTS = list(VALID_CHOICES.keys())
VALID_CHOICES_VALUES = list(VALID_CHOICES.values())

def determine_winner(player_choice, computer_choice):
    '''
    Prints a message indicating who won (player or computer) depending on player
    and computer choices
    '''
    # player win conditions
    if ((player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'rock' and computer_choice == 'lizard') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'paper' and computer_choice == 'spock') or
        (player_choice == 'scissors' and computer_choice == 'paper') or
        (player_choice == 'scissors' and computer_choice == 'lizard') or
        (player_choice == 'spock' and computer_choice == 'scissors') or
        (player_choice == 'spock' and computer_choice == 'rock') or
        (player_choice == 'lizard' and computer_choice == 'paper') or
        (player_choice == 'lizard' and computer_choice == 'spock')):
        print('You win!')
    # computer win conditions
    elif ((player_choice == 'rock' and computer_choice == 'spock') or
        (player_choice == 'rock' and computer_choice == 'paper') or
        (player_choice == 'paper' and computer_choice == 'lizard') or
        (player_choice == 'paper' and computer_choice == 'scissors') or
        (player_choice == 'scissors' and computer_choice == 'spock') or
        (player_choice == 'scissors' and computer_choice == 'rock') or
        (player_choice == 'spock' and computer_choice == 'lizard') or
        (player_choice == 'spock' and computer_choice == 'paper') or
        (player_choice == 'lizard' and computer_choice == 'rock') or
        (player_choice == 'lizard' and computer_choice == 'scissors')):
        print('Computer wins!')
    # tie
    else:
        print('It\'s a tie!')


# game
while True:
    os.system('clear')

    # user chooses from valid choices
    while True:
        player_choice = input((f'==> Please choose one: '
                              f'{', '.join(VALID_CHOICES_SHORTCUTS)} for'
                              f' {', '.join(VALID_CHOICES_VALUES)}\n'))
        if player_choice in VALID_CHOICES_SHORTCUTS:
            break
        print('That wasn\'t a valid choice.')

    computer_choice = random.choice(VALID_CHOICES_VALUES)

    print(f'==> You chose {VALID_CHOICES[player_choice]}, the computer chose'
          f' {computer_choice}.')

    determine_winner(VALID_CHOICES[player_choice], computer_choice)

    # user decides whether to continue playing the game or to stop
    while True:
        user_plays_again = input('==> Do you want to play again? y/n\n')
        if user_plays_again.lower() in ['y', 'n']:
            break
        print('Invalid input. Please enter y/n')

    if user_plays_again.lower() == 'n':
        print('Thanks for playing. Closing program.')
        time.sleep(1.5)
        os.system('clear')
        break
