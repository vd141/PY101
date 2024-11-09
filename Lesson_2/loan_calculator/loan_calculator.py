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

def valid_input(num):
    '''
    Checks if num string can be coerced into a float. If so, checks if float is
    non-negative.
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

def get_loan_dollars():
    '''
    Gets loan amount from user and reprompts if input is invalid
    '''
    loan_dollars_input = input('==> Please enter the dollar amount of the '
                         'loan:\n')
    while not valid_input(loan_dollars_input):
        loan_dollars_input = input('==> Please enter the dollar amount of the '
                             'loan:\n')
    return float(loan_dollars_input)

def get_apr_percent():
    '''
    Gets apr percent from user and reprompts if input is invalid
    '''
    apr_percent_input = input('==> Please enter the APR of the loan '
                        '(e.g. 5 for 5%):\n')
    while not valid_input(apr_percent_input):
        apr_percent_input = input('==> Please enter the APR of the loan '
                            '(e.g. 5 for 5%):\n')
    return float(apr_percent_input)

def get_loan_months():
    '''
    gets loan duration in months from user and reprompts if input is invalid
    '''
    loan_months_input = input('==> Please enter the duration of the loan in whole '
                        'months:\n')
    while not valid_input(loan_months_input):
        loan_months_input = input('==> Please enter the duration of the loan in '
                        'whole months:\n')
    return float(loan_months_input)


reuse_calc = True
print('==> Welcome to Loan Calculator!')

while reuse_calc:
    loan_dollars = get_loan_dollars()

    apr_percent = get_apr_percent()

    loan_months = get_loan_months()

    monthly_interest_rate = apr_percent / (12 * 100)

    monthly_payment = loan_dollars * (monthly_interest_rate /
                                    (1 - (1 + monthly_interest_rate)
                                    ** -loan_months))

    print(f'==> The monthly payment is ${monthly_payment:.2f}.')

    reuse_calc_input = input('==> Would you like to use '
                    'the loan_calculator again? y/n\n')

    if reuse_calc_input != 'y':
        print('==> I hope you enjoyed using Loan Calculator. Goodbye.')
        reuse_calc = False
