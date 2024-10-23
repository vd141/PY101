# Odd Numbers
# print all odd numbers from 1 to 99, inclusive, with each number
# on a separate line

for i in range(1, 100):
    print(i)

# Bonus Question: Can you solve the problem by iterating over just
# the odd numbers?

for i in range(1, 100, 2):
    print(i)

# Further Exploration:
# consider adding a way for the user to specify the starting and
# ending values of the odd numbers printed

starting_value = int(input("Please tell me your starting value: "))
ending_value = int(input('Please tell me your ending value: '))
for i in range(starting_value, ending_value+1, 2):
    print(i)

# TODO: add code to address the edge case where a user inputs an even number