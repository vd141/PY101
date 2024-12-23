'''
What does each code snippet print?
'''

#1 
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
'''
the local variables one, two, three are initialized to point to each of the arguments.
each local variable is reassigned. reassignments do not mutate the lists

no mutations are being made in the function, so the mutable arguments are unchanged.
# one is: ["one"]
# two is: ["two"]
# three is: ["three"]
'''

#2
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
'''
again, the local variables inside the function are being reassigned. these 
do not mutate the lists in the global scope
# one is: ["one"]
# two is: ["two"]
# three is: ["three"]
'''

#3
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
'''
the arguments are being mutated by the function because the elements are being reassigned
in the function. lists in python are mutable and passed by reference, so the changes
are reflected outside the function
# one is: ["two"]
# two is: ["three"]
# three is: ["one"]
'''
