'''
Alan wrote the following function, which was intended to return all of the 
factors of number.

How can this function take negative numbers?

Without changing any of the logic in the while loop, I could coerce the input to
be positive if it is negative. Once all the positive factors are found, I can 
add the negative factors to that output by adding negative counterparts of all
positive factors

number % divisor checks if the divisor is a factor
'''

def factors(number):
    divisor = abs(number)
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    if abs(number) == number:
        return result
    else:
        return result + [-num for num in result]
    

print(factors(-100))