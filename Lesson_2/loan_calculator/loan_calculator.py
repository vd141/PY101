''' determine the monthly payment assuming the interest is compounded monthly
 
  3 pieces of information are needed:
  - the loan amount
  - the annual percentage rate (APR)
  - the loan duration

  from the above, calculate the
  - monthly interest rate (APR/12)
  - loan duration in months

ask the user for the loan amount in dollars
ask the user for the APR in percentage points
ask the user for the loan duration in months
'''

import os
import time

MONTHS_IN_YEAR = 12
PERCENT_DENONMINATOR = 100

def valid_positive_float_input(num):
    '''
    Checks if num string can be coerced into a float. If so, checks if float is
    greater than 0.
    '''
    try:
        num = float(num)
        if num <= 0:
            print(f'==> {num} is invalid. Please enter a positive number.')
            return False
    except ValueError:
        print(f'==> {num} is invalid. Please enter a numeric value.')
        return False
    return True

def valid_nonnegative_float_input(num):
    '''
    Checks if num string can be coerced into a float. If so, checks if float is
    non-negative.
    '''
    try:
        num = float(num)
        if num < 0:
            print(f'==> {num} is invalid. Please enter a nonnegative number.')
            return False
    except ValueError:
        print(f'==> {num} is invalid. Please enter a numeric value.')
        return False
    return True

def get_loan_dollars():
    '''
    Gets loan amount from user and reprompts if input is invalid
    '''
    while True:
        loan_dollars_input = input('==> Please enter the dollar amount of the '
                                   'loan:\n')
        if valid_positive_float_input(loan_dollars_input):
            return float(loan_dollars_input)

def get_apr_percent():
    '''
    Gets apr percent from user and reprompts if input is invalid
    '''
    while True:
        apr_percent_input = input('==> Please enter the APR of the loan '
                                  '(e.g. 5 for 5%):\n')
        if valid_nonnegative_float_input(apr_percent_input):
            return float(apr_percent_input)

def get_loan_months():
    '''
    gets loan duration in months from user and reprompts if input is invalid
    '''
    while True:
        loan_months_input = input('==> Please enter the duration of the loan in'
                                  ' whole months:\n')
        if valid_positive_float_input(loan_months_input):
            return float(loan_months_input)

def calculate_monthly_payment(loan_dollars, monthly_interest_rate, loan_months):
    '''
    Calculates and returns the monthly payment from the three parameters. Can
    accept a 0 APR loan.
    '''
    if monthly_interest_rate > 0:
        return (loan_dollars * (monthly_interest_rate /
                                (1 - (1 + monthly_interest_rate)
                                ** -loan_months)))
    else:
        return (loan_dollars / loan_months)

def valid_calc_reuse(input_):
    '''
    validate calculator reuse input. Returns True if input is valid, returns
    False if not
    '''
    if input_ in ['y', 'n']:
        return True
    print('Invalid input. Please enter y/n.')
    return False

def reuse_calc():
    '''
    Returns True if the input is 'y', False if it does not
    '''
    while True:
        reuse_calc_input = input('==> Would you like to use the loan calculator'
                                 ' again? y/n\n')
        if valid_calc_reuse(reuse_calc_input):
            if reuse_calc_input == 'y':
                return True
            return False

def closing_countdown_timer(seconds):
    '''
    Counts down from the number of seconds and clears the console.
    '''
    print('==> I hope you enjoyed using Loan Calculator. Closing in...')
    for second in range(seconds, 0, -1):
        time.sleep(1)
        print(second)
    time.sleep(1)
    print('Goodbye!')
    time.sleep(1.5)
    os.system('clear')


while True:
    os.system('clear')

    print('==> Welcome to Loan Calculator!')

    loan_dollars = get_loan_dollars()

    apr_percent = get_apr_percent()

    loan_months = get_loan_months()

    monthly_interest_rate = apr_percent / (MONTHS_IN_YEAR *
                                           PERCENT_DENONMINATOR)

    monthly_payment = calculate_monthly_payment(loan_dollars,
                                                monthly_interest_rate,
                                                loan_months)

    print(f'==> The monthly payment is ${monthly_payment:.2f}.')

    if reuse_calc():
        continue
    closing_countdown_timer(3)
    break
