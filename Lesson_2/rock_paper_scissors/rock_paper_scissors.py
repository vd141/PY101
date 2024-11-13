'''
1. The user makes a choice.
2. The computer makes a choice.
3. A winner is displayed.
'''

import random
import os
import time

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def determine_winner(player_choice, computer_choice):
    '''
    Prints a message indicating who won (player or computer) depending on player
    and computer choices
    '''
    # player win conditions
    if ((player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')):
        print('You win!')
    # computer win conditions
    elif ((player_choice == 'rock' and computer_choice == 'paper') or
        (player_choice == 'paper' and computer_choice == 'scissors') or
        (player_choice == 'scissors' and computer_choice == 'rock')):
        print('Computer wins!')
    # tie
    else:
        print('It\'s a tie!')


# game
while True:
    os.system('clear')

    # user chooses from valid choices
    while True:
        player_choice = input(f'==> Please choose one: '
                            '{', '.join(VALID_CHOICES)}\n')
        if player_choice in VALID_CHOICES:
            break
        print('That wasn\'t a valid choice.')

    computer_choice = random.choice(VALID_CHOICES)

    print(f'==> You chose {player_choice}, the computer chose'
          ' {computer_choice}.')

    determine_winner(player_choice, computer_choice)

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
