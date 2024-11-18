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

BEST_OF_FIVE_ROUNDS = 3
CLOSING_SECONDS = 8
VALID_CHOICES = {'r': 'rock',
                 'p': 'paper',
                 'sc': 'scissors',
                 'l': 'lizard',
                 'sp': 'spock',
                 }
VALID_CHOICES_SHORTCUTS = list(VALID_CHOICES.keys())
VALID_CHOICES_VALUES = list(VALID_CHOICES.values())


def player_chooses():
    '''
    Gets input from user, and reprompts for input if input was invalid
    '''
    # user chooses from valid choices
    while True:
        player_choice = input((f'==> Please choose one: '
                            f'{', '.join(VALID_CHOICES_SHORTCUTS)} for'
                            f' {', '.join(VALID_CHOICES_VALUES)}\n'))
        player_choice = player_choice.lower()
        if player_choice in VALID_CHOICES_SHORTCUTS:
            break
        print('==> That wasn\'t a valid choice.')

    return player_choice


def computer_chooses():
    '''
    Computer chooses randomly from available choices.
    '''
    return random.choice(VALID_CHOICES_VALUES)


def display_choices(player_choice, computer_choice):
    '''
    Prints both user and computer choices to the console
    '''
    print(f'==> You chose {VALID_CHOICES[player_choice]}, the computer chose'
          f' {computer_choice}.')

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
        print('==> You won the round!')
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
        print('==> Computer won the round!')
        return [0, 1]
    # tie
    else:
        print('==> That round ended in a tie!')
        return [0, 0]


def tally_score(result, cumulative_results):
    '''
    Updates cumulative result with current result
    '''
    cumulative_results[0] += result[0]
    cumulative_results[1] += result[1]


def print_game_winner(cumulative_results):
    '''
    Prints game results, assuming game is concluding
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


def won_best_of_five(cumulative_results):
    '''
    Returns True if computer or user won best of 5 (3 wins)
    '''
    if (BEST_OF_FIVE_ROUNDS in [cumulative_results[0],
                                    cumulative_results[1]]):
        return True
    return False


def print_current_score(cumulative_results):
    '''
    Prints cumulative results
    '''
    print(f'==> The score is currently:\n==> You: {cumulative_results[0]} '
                f'Computer: {cumulative_results[1]}')


def play_again(cumulative_results):
    '''
    Prompt user to play again.
    '''
    while True:
        print_current_score(cumulative_results)
        user_plays_again = input('==> Do you want to play again? y/n\n')
        if user_plays_again.lower() in ['y', 'n']:
            return user_plays_again.lower()
        print('==> Invalid input. Please enter y/n')


def display_game_end_sequence(cumulative_results):
    '''
    Print final results and prepare to end game.
    '''
    print_game_winner(cumulative_results)
    print(f'==> Thanks for playing. Closing program in...')
    for second in range(CLOSING_SECONDS, -1, -1):
        print(f'\r{second} seconds', end = '')
        time.sleep(1)
    os.system('clear')


def play_rock_paper_scissors():
    '''
    Main game logic
    '''
    cumulative_results = [0, 0]

    # game
    while True:
        os.system('clear')

        player_choice = player_chooses()
        computer_choice = computer_chooses()

        display_choices(player_choice, computer_choice)

        result = determine_round_winner(VALID_CHOICES[player_choice],
                                        computer_choice)

        tally_score(result, cumulative_results)

        if won_best_of_five(cumulative_results):
            display_game_end_sequence(cumulative_results)
            break

        if play_again(cumulative_results) == 'n':
            display_game_end_sequence(cumulative_results)
            break

play_rock_paper_scissors()
