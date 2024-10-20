# floating point arithmetic
# write a program that prompts the user for two foating point positive numbers,
# then prints the results of the following operations on those two numbers:
# addition, subtraction, product, quotient, floor quotient, remainder, and 
# power. Do not worry about validating the input

float_1 = float(input('==> Enter the first number: \n'))
float_2 = float(input('==> Enter the second number: \n'))

print(f'==> {float_1:.6f} + {float_2:.6f} = {(float_1 + float_2):.6f}')
print(f'==> {float_1:.6f} - {float_2:.6f} = {(float_1 - float_2):.6f}')
print(f'==> {float_1:.6f} * {float_2:.6f} = {(float_1 * float_2):.6f}')
print(f'==> {float_1:.6f} / {float_2:.6f} = {(float_1 / float_2):.6f}')
print(f'==> {float_1:.6f} // {float_2:.6f} = {(float_1 // float_2):.6f}')
print(f'==> {float_1:.6f} % {float_2:.6f} = {(float_1 % float_2):.6f}')
print(f'==> {float_1:.6f} ** {float_2:.6f} = {(float_1 ** float_2):.6f}')