'''
alan wrote the following function, which is supposed to return all the factors
of number

Alyssa noticed that this code would fail when the input is a negative number, and
asked Alan to change the loop. How can he make this work? Note that we're not 
looking to find the factors for negative numbers, but we want to handle it
gracefully instead of going into an infinite loop

Bonus question: what does number % divisor == 0 do in the code?
'''
def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
'''
it should work with only positive numbers. it should always work with the absolute
value of the input, by using the abs() function

number % divisor == 0 checks to see if the candidate divisor is a factor of number.
that statement returns a boolean
'''