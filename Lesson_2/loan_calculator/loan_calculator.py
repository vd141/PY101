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

# TODO: encapsulate code in custom functions

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

reuse_calc = True
print('==> Welcome to Loan Calculator!')

while reuse_calc:
    loan_dollars = input('==> Please enter the dollar amount of the loan:\n')
    while not valid_input(loan_dollars):
        loan_dollars = input('==> Please enter the dollar amount of the loan:\n')

    apr_percent = input('==> Please enter the APR of the loan (e.g. 5 for 5%):\n')
    while not valid_input(apr_percent):
        apr_percent = input('==> Please enter the APR of the loan (e.g. 5 for 5%):\n')

    loan_months = input('==> Please enter the duration of the loan in whole '
                        'months:\n')
    while not valid_input(loan_months):
        loan_months = input('==> Please enter the duration of the loan in whole '
                        'months:\n')

    loan_dollars = float(loan_dollars)
    apr_percent = float(apr_percent)
    loan_months = int(loan_months)

    monthly_interest_rate = apr_percent/(12 * 100)

    monthly_payment = loan_dollars * (monthly_interest_rate /
                                    (1 - (1 + monthly_interest_rate)
                                    ** -loan_months))

    print(f'==> The monthly payment is ${monthly_payment:.2f}.')

    reuse_calc_input = input('==> Would you like to use '
                    'the loan_calculator again? y/n\n')

    if reuse_calc_input != 'y':
        print('==> I hope you enjoyed using Loan Calculator. Goodbye.')
        reuse_calc = False