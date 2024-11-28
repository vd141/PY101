'''
How would you verify whether the data structures assigned to the variables
numbers and table are of type list?
'''
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
'''
we can use the type function or the isinstance function

the type function returns a type object that describes what type the argument is

the isinstance function takes two arguments, the object we would like to find the 
type of and a type ob indicating the type we would like to check for. it returns a boolean
'''
print(isinstance(numbers, list))
print(isinstance(table, list))