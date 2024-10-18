# Multiples of 3 and 5

# Write a function that computes the sum of all numbers between 1 and some other
# number, inclusive, that are multiples of 3 or 5.

# assume that the number passed in is an integer greater than 1

def multisum(upper_boundary):
    sum = 0
    for i in range(1, upper_boundary+1):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return sum

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)