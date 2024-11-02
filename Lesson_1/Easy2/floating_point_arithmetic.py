# floating point arithmetic
# write a program that prompts the user for two foating point positive numbers,
# then prints the results of the following operations on those two numbers:
# addition, subtraction, product, quotient, floor quotient, remainder, and 
# power. Do not worry about validating the input
# MODULARIZE

# float_1 = float(input('==> Enter the first number: \n'))
# float_2 = float(input('==> Enter the second number: \n'))

# def expression(float1, float2, operation):
#     return f'==> {float1:.6f} {operation} {float2:.6f} ='

# def calculation(float1, float2, operation):
#     match operation:
#         case '+': return float1 + float2
#         case '-': return float1 - float2
#         case '*': return float1 * float2
#         case '/': return float1 / float2
#         case '//': return float1 // float2
#         case '%': return float1 % float2
#         case '**': return float1 ** float2

# for operation in ['+', '-', '*', '/', '//', '%', '**']:
#     print(f'{expression(float_1, float_2, operation)} '
#           f'{calculation(float_1, float_2, operation):6f}')

def prompt(string):
    return f'==> {string}'

def calculation(operation, first_number, second_number):
    first_number = float(first_number)
    second_number = float(second_number)

    match operation:
            case '+':
                return first_number + second_number
            case '-':
                return first_number - second_number
            case '*':
                return first_number * second_number
            case '/':
                return first_number / second_number
            case '//':
                return first_number // second_number
            case '%':
                return first_number % second_number
            case '**':
                return first_number ** second_number

welcome_prompt = prompt('Welcome to floating point arithmetic calculator!')
first_prompt = prompt('Enter the first number:\n')
second_prompt = prompt('Enter the second number:\n')

print(welcome_prompt)
first_number = input(first_prompt)
second_number = input(second_prompt)

operations = ['+', '-', '*', '/', '//', '%', '**']

for operation in operations:
    result = calculation(operation, first_number, second_number)
    result_prompt = prompt(f'{first_number} {operation} {second_number} '
                           f'= {result}')
    print(result_prompt)