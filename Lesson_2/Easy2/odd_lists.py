# write a function that returns a list that contains every other element of a
# list that is passed in as an argument. The values in the returned list should
# be those values that are in the 1st, 3rd, 5th, and so on elements of the 
# argument list

# we can use the range lazy data structure to iterate through the length of the 
# list, grabbing every 1st, 3rd, 5th, and so on element. append these to a new
# list and return the list

# if the collection is length of 4: [0 1 2 3]
# if the collectino is length of 5: [0 1 2 3 4]

def oddities(collection):
    # odd_list = []

    # for i in range(0, len(collection), 2):
    #     odd_list.append(collection[i])

    # return odd_list

    # using list slicing
    return collection[::2]

def evenities(collection):
    return collection[1::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

print(evenities([2, 3, 4, 5, 6]) == [3, 5])  # True
print(evenities([1, 2, 3, 4]) == [2, 4])        # True
print(evenities(["abc", "def"]) == ['def'])     # True
print(evenities([123]) == [])                # True
print(evenities([]) == [])                      # True