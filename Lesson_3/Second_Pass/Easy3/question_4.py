'''
What will the following code output?
'''
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
'''
my_list1 is a variable that is assigned to a list of heterogenous values
my_list2 is a shallow copy of my_list1. That means the outer object (the list)
is a different object, but its elements are the same objects that were in the 
first list

after the first two lines, my_list2.append(1) will mutate my_list2, but leave
my_list1 unmutated

however, if we mutate an element of my_list2, it will affect the same element in 
my_list1

the statement my_list2[0]['first'] = 42 mutates the value of the first dict, which
both my_list1 and my_list2 point to

print(my_list1) will print
# [{"first": 42}, {"second": "value2"}, 3, 4, 5]
'''