'''
Write two distinct ways of reversing the list without mutating the original list
'''
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
'''
One way is to use slicing. We can use the syntax numbers[::-1] to return a new list with all the elements reversed

Another way is to use the reversed() function. This returns a lazy sequence with all of the elements reversed. The list contsructor must be invoked to convert
this lazy sequence into a list.
'''
print(numbers[::-1])
print(numbers)
print(list(reversed(numbers)))
print(numbers)