# ask the user for the first number
# ask the user for the second number
# ask the user for the type of operation to perform: add, subtract, multiply, or 
# divide
# perform the calculation and display the result

print('Welcome to Calculator!')
first_number = input('Enter the first number:\n')
second_number = input('Enter the second number:\n')
operation = input('1) add, 2) subtract, 3) multiply, 4) divide \n')

match operation:
    case '1':
        result = float(first_number) + float(second_number)
    case '2':
        result = float(first_number) - float(second_number)
    case '3':
        result = float(first_number) * float(second_number)
    case '4':
        result = float(first_number) / float(second_number)

print(f'\n{result} is the result.')