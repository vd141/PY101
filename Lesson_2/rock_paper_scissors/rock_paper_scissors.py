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

def determine_round_winner(player_choice, computer_choice):
    '''
    Prints a message indicating who won (player or computer) depending on player
    and computer choices

    returns a 1x2 list indicating the winner of that round
    player wins:   [1, 0]
    computer wins: [0, 1]
    tie:           [0, 0]
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
        print('==> You win!')
        return [1, 0]
    # computer win conditions
    if ((player_choice == 'rock' and computer_choice == 'spock') or
        (player_choice == 'rock' and computer_choice == 'paper') or
        (player_choice == 'paper' and computer_choice == 'lizard') or
        (player_choice == 'paper' and computer_choice == 'scissors') or
        (player_choice == 'scissors' and computer_choice == 'spock') or
        (player_choice == 'scissors' and computer_choice == 'rock') or
        (player_choice == 'spock' and computer_choice == 'lizard') or
        (player_choice == 'spock' and computer_choice == 'paper') or
        (player_choice == 'lizard' and computer_choice == 'rock') or
        (player_choice == 'lizard' and computer_choice == 'scissors')):
        print('==> Computer wins!')
        return [0, 1]
    # tie
    else:
        print('==> It\'s a tie!')
        return [0, 0]

def tally_score(result, cumulative_results):
    '''
    Updates cumulative result with current result
    '''
    cumulative_results[0] += result[0]
    cumulative_results[1] += result[1]

def determine_game_winner(cumulative_results):
    '''
    Prints game results
    '''
    str_cumulative_results = list(map(str, cumulative_results))
    if cumulative_results[0] > cumulative_results[1]:
        print(f'==> You win the game {cumulative_results[0]}-'
              f'{cumulative_results[1]}!')
    elif cumulative_results[1] > cumulative_results[0]:
        print(f'==> The computer wins the game {cumulative_results[1]}-'
              f'{cumulative_results[0]}!')
    else:
        print(f'==> You and the computer tied '
              f'{'-'.join(str_cumulative_results)}!')

def play_game():

    cumulative_results = [0, 0]

    # game
    while True:
        os.system('clear')

        # user chooses from valid choices
        while True:
            player_choice = input((f'==> Please choose one: '
                                f'{', '.join(VALID_CHOICES_SHORTCUTS)} for'
                                f' {', '.join(VALID_CHOICES_VALUES)}\n'))
            player_choice = player_choice.lower()
            if player_choice in VALID_CHOICES_SHORTCUTS:
                break
            print('==> That wasn\'t a valid choice.')

        computer_choice = random.choice(VALID_CHOICES_VALUES)

        print(f'==> You chose {VALID_CHOICES[player_choice]}, the computer chose'
            f' {computer_choice}.')

        result = determine_round_winner(VALID_CHOICES[player_choice], computer_choice)
        tally_score(result, cumulative_results)

        if (cumulative_results[0] == 3) or (cumulative_results[1] == 3):
            determine_game_winner(cumulative_results)
            break

        # user decides whether to continue playing the game or to stop
        while True:
            print(f'==> The score is currently:\n==> You: {cumulative_results[0]} '
                f'Computer: {cumulative_results[1]}')
            user_plays_again = input('==> Do you want to play again? y/n\n')
            if user_plays_again.lower() in ['y', 'n']:
                break
            print('==> Invalid input. Please enter y/n')

        if user_plays_again.lower() == 'n':
            determine_game_winner(cumulative_results)
            print('==> Thanks for playing. Closing program...')
            time.sleep(4)
            os.system('clear')
            break
