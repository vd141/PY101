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

loan_dollars = input('==> Please enter the dollar amount of the loan:\n')
apr_percent = input('==> Please enter the APR of the loan (e.g. 5 for 5%):\n')
loan_months = input('==> Please enter the duration of the loan in whole '
                    'months:\n')

loan_dollars = float(loan_dollars)
apr_percent = float(apr_percent)
loan_months = int(loan_months)

monthly_interest_rate = apr_percent/(12 * 100)

monthly_payment = loan_dollars * (monthly_interest_rate /
                                  (1 - (1 + monthly_interest_rate)
                                   ** -loan_months))

print(f'The monthly payment is ${monthly_payment:.2f}.')
