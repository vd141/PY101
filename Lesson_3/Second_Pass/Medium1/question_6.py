'''
What is the output of the following code?
'''
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)
'''
the mess with it function takes answer as an argument and returns the sum of answer
and 8. this returned value is assigned to the variable new_answer

answer is not mutated by the function as integers are immutable. and it is not 
reassigned to a new value inside the function. so the value of answer remains
42 after the function is invoked.

the final line prints answer (42) - 8, which is 34
# 34
'''