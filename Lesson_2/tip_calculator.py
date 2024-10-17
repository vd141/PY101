# Tip Calculator
# The program should prompt for a bill amount and a tip rate. The program must 
# compute the tip, then print both the tip and the total amount of the bill.

def calculate_tip():
    bill = float(input('What is the bill? '))
    tip_percentage = float(input('What is the tip percentage? '))

    tip = bill * (tip_percentage / 100)
    total = tip + bill

    print(f'The tip is ${tip:.2f}')
    print(f'The total is ${total:.2f}')

calculate_tip()